import hos_heroes

input_file_name = input("enter source code file name : ")
f = open("{0}.hos".format(input_file_name))
codelines = f.readlines()

variables = {}
judge = 0
truelineplus = 0
onephase = 0
originop = 0
line = 1
while line < len(codelines):
    eofcheck = codelines[line]

    if eofcheck == 'nexus':
        break

    rc = [codelines[line][:-1], codelines[line + 1][:-1], codelines[line + 2][:-1], codelines[line + 3][:-1]]
    print(rc)
    if rc[0][rc[0].find(';') + 1:] == 'compositionb' and judge == 1 and truelineplus != 0:  # if 제어문 분기점 검사
        truelineplus -= 4
        rc = ['', '', '', '']

    if rc[0][rc[0].find(';') + 1:] == 'compositiona' and judge == 0:
        rc = ['', '', '', '']

    if rc[0][rc[0].find(';') + 1:] == 'compositiona' and judge == 1 and onephase != 0:
        onephase -= 4
        if onephase == 0:
            line = line - (originop+4)
            judge = 0
            originop = 0


    if rc[0][:8] == 'Tassadar':
        ta = hos_heroes.Tassadar(rc[2])

        if rc[1][:11] == 'psiinfusion':
            ta.psiinfusion(variables, rc[3], rc[1][12:])

            if rc[1][12:] == 'templarswill':
                ta.psiinfusion(variables, ta.templarswill(variables, rc[3], rc[1][25:]))

    if rc[0][:7] == 'Artanis':        # 리스트 관련 빌트인
        ar = hos_heroes.Artanis()

        if rc[1][:6] == 'append':
            ar.append(variables, rc[2], rc[3], rc[1][7:13], rc[14:])

        if rc[1][:9] == 'listsorts':
            ar.listsorts(variables, rc[2], rc[1][10:])

        if rc[1][:3] == 'pop':
            ar.pop(variables, rc[2], rc[3])

        if rc[1][:5] == 'count':
            anum = rc[2].split("storm")
            ar.count(variables, anum[0], anum[1], rc[3], rc[1][6:])

    if rc[0][:5] == 'Jaina':
        ja = hos_heroes.Jaina()

        if rc[1][:9] == 'frostbolt':
            ja.frostbolt(variables, rc[2], float(rc[3]), rc[1][10:])

        if rc[1][:15] == 'arcaneintellect':
            ab = rc[2].split("storm")
            ja.arcaneintellect(variables, ab[0], ab[1], rc[3], rc[1][17:])

    if rc[0][:7] == 'Tracer':
        absplit = rc[2].split("storm")
        ts = hos_heroes.Tracer(absplit[0], absplit[1])

        if rc[1][:11] == 'spatialecho':
            gotolinesplit = rc[3].split("storm")
            judge = ts.spatialecho(variables, rc[1][12:], line, gotolinesplit[0])  # false일경우 line += gotolinesplit[0]
            truelineplus = int(gotolinesplit[1])

        if rc[1][:11] == 'totalrecall':
            judge = ts.totalrecall(variables, rc[1][12:], line)
            onephase = int(rc[3])
            originop = int(rc[3])

    if rc[0][:9] == 'Ragnaros':
        ra = hos_heroes.Ragnaros()

        if rc[1][:12] == 'livingmeteor':
            ra.livingmeteor(variables, rc[1][13:], rc[2])

        if rc[1][:14] == 'handofragnaros':
            variables[rc[3]] = ra.handofragnaros(rc[1][15:], rc[2])

    line += 4
    print(variables)
