GradeFile = open("GradeFile.txt", "r")
FinalFile = open("Complete.txt", "w")
FinalFileSlim = open("CompleteSlim.txt", "w")


def AgglomerateCalculation(Compiled_Dict):
    # This function should loop through the dict entries in order to calculate total grade, and the minimum needed from
    # assignments (in each catagory) of weights 10, 20, 50, 100, and 200 to keep the grade at 89.5, 79.5, and 69.5
    GradeGoals = [89.5, 79.5, 69.5]
    AssignWeights = [10, 20, 50, 100, 200]
    curr_compscore = []
    FinalScoreDict = {}
    FinalScoreList = []
    base_total = TotalGradeCalc(Compiled_Dict)
    print base_total
    baseline_dict = Compiled_Dict
    for item in baseline_dict:
        curr_compscore.append(TotalGradeExcept(Compiled_Dict, item))
        for score in GradeGoals:
            base_need = BaselineScoreCalc(curr_compscore[item], score, baseline_dict[item][0])
            FinalScoreList = []
            for asweight in AssignWeights:
                final_need = FinalGradeCalc(baseline_dict[item][1], base_need, asweight, baseline_dict[item][2])
                FinalScoreList.append((asweight, final_need))
            FinalScoreDict[(item, score)] = FinalScoreList
    return FinalScoreDict


def ScoreCompiler(Raw_Dict):
    Compiled_Dict = {}
    for catag in Raw_Dict:
        score_total = 0
        score_count = 0
        weight_total = 0
        weight_count = 0
        count_track = 0
        for score in Raw_Dict[catag][1]:
            for num in range(1, Raw_Dict[catag][2][count_track]):
                score_total += score
                score_count += 1
            count_track += 1
        score_avg = float(score_total) / float(score_count)
        for weight in Raw_Dict[catag][2]:
            weight_total += weight
            weight_count += 1
        weight_avg = float(weight_total) / float(weight_count)
        Compiled_Dict[catag] = (Raw_Dict[catag][0], score_avg, weight_total)
    return Compiled_Dict


def TextParse():
    line_track = 0
    total_weight = 0
    subscores = []
    subweights = []
    raw_dict = {}
    catagory_dictnum = 0
    for line in GradeFile:
        line_track += 1
        temp_comp = line.split()
        if line_track == 1:
            total_weight = int(line)
        if line_track == 2:
            for score in temp_comp:
                subscores.append(int(score))
        if line_track == 3:
            for weight in temp_comp:
                subweights.append(int(weight))
        if line_track >= 3:
            value_list = [total_weight, subscores, subweights]
            raw_dict[catagory_dictnum] = value_list
            subscores = []
            subweights = []
            catagory_dictnum += 1
            line_track = 0
    return raw_dict


def TotalGradeCalc(Compiled_Dict):
    temp_dict = Compiled_Dict
    total_grade_score = 0
    total_grade_count = 0
    total_weight = 0
    for comp_score in temp_dict:
        for count in range(1, temp_dict[comp_score][0]):
            total_grade_score += temp_dict[comp_score][1]
            total_grade_count += 1
        total_weight += float(temp_dict[comp_score][2]) / float(temp_dict[comp_score][0])
    total_grade = float(total_grade_score) / float(total_grade_count)
    return total_grade


def TotalGradeExcept(Compiled_Dict, ExcludedKey):
    temp_dict = Compiled_Dict
    total_grade_score = 0
    total_grade_count = 0
    total_weight = 0
    for comp_score in temp_dict:
        if comp_score != ExcludedKey:
            for count in range(1, temp_dict[comp_score][0]):
                total_grade_score += temp_dict[comp_score][1]
                total_grade_count += 1
            total_weight += float(temp_dict[comp_score][2]) / float(temp_dict[comp_score][0])
    total_grade = float(total_grade_score) / float(total_grade_count)
    return total_grade


def BaselineScoreCalc(current_score, needed_score, comp_weight):
    difference = needed_score - current_score
    adjust_diff = difference * (1 / (float(comp_weight) / 100))
    needed_compscore = adjust_diff + current_score
    return needed_compscore


def FinalGradeCalc(current_score, needed_score, comp_weight, total_weight):
    difference = needed_score - current_score
    adjust_diff = difference * (1 / (float(comp_weight) / float(total_weight)))
    needed_compscore = adjust_diff + current_score
    return needed_compscore


def FileWriter(FinalGradesDict):
    for reqgrades in FinalGradesDict:
        FinalFile.write("Category " + str(reqgrades[0] + 1) + ": To Get " + str(reqgrades[1]) + "\n")
        FinalFileSlim.write("Category " + str(reqgrades[0] + 1) + ": To Get " + str(reqgrades[1]) + "\n")
        for grade in FinalGradesDict[reqgrades]:
            FinalFile.write("Assignment Weight " + str(grade[0]) + " | Grade Needed " + str(grade[1]) + "\n")
            if grade[1] >= 0 and grade[1] <= 100:
                FinalFileSlim.write("Assignment Weight " + str(grade[0]) + " | Grade Needed " + str(grade[1]) + "\n")


FileWriter(AgglomerateCalculation(ScoreCompiler(TextParse())))

execfile("Looper.py")

import os
os.startfile("Complete.txt",'open')


