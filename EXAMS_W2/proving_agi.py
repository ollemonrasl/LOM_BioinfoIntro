import csv

agi_lg_list = []
agi_g_list = []

with open("/home/osboxes/BioinformaticsCourseGit/LOM_BioinfoIntro/EXAMS_W2/LocusGene.tsv") as lg_tsvfile:
    lg = csv.reader(lg_tsvfile, delimiter = "\t", quotechar = '"')
    for row in lg:
        agi_lg_list.append(row[0])

with open("/home/osboxes/BioinformaticsCourseGit/LOM_BioinfoIntro/EXAMS_W2/Germplasm.tsv") as g_tsvfile:
    g = csv.reader(g_tsvfile, delimiter = "\t", quotechar = "'")
    for row in g:
        agi_g_list.append(row[0])

for index in range(len(agi_lg_list)):
    if agi_lg_list[index] == agi_g_list[index]:
        pass
    else:
        print(agi_lg_list[index] + " and " + agi_g_list[index])
