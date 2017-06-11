import hos_heroes

input_file_name = input("enter source code file name : ")
f = open("{0}.hos".format(input_file_name))
codelines = f.readlines()

variables = {}
judge = 0
truelineplus = 0

for line in range(1, len(codelines), 4):

    eofcheck = codelines[line]
    if eofcheck == 'nexus':
        break

    rc = [codelines[line][:-1], codelines[line + 1][:-1], codelines[line + 2][:-1], codelines[line + 3][:-1]]

    if rc[0][rc[0].find(';') + 1:] == 'compositionb' and judge == 1 and truelineplus != 0:  # if 제어문 분기점 검사
        truelineplus -= 4
        rc = ['', '', '', '']

    if rc[0][:8] == 'Tassadar':
        ta = hos_heroes.Tassadar(rc[2])
        if rc[1][:11] == 'psiinfusion':
            ta.psiinfusion(variables, rc[3], rc[1][12:])

            if rc[1][12:] == 'psiinfusion;templarswill':
                ta.psiinfusion(variables, ta.templarswill(variables, rc[3], rc[1][25:]))

    if rc[0][:6] == 'Jaina':
        ja = hos_heroes.Jaina()
        if rc[1][:10] == 'frostbolt':
            ja.frostbolt(variables, rc[2], float(rc[3]), rc[1][10:])

    if rc[0][:7] == 'Tracer':
        absplit = rc[2].split("storm")
        ts = hos_heroes.Tracer(absplit[0], absplit[1])
        gotolinesplit = rc[3].split("storm")

        if rc[1][:11] == 'spatialecho':
            judge = ts.spatialecho(variables, rc[1][12:], line, gotolinesplit[0])  # false일경우 line += gotolinesplit[0]
            truelineplus = int(gotolinesplit[1])
        if rc[1][:12] == 'totalrecall':
            pass

    if rc[0][:9] == 'Ragnaros':
        ra = hos_heroes.Ragnaros()

        if rc[1][:12] == 'livingmeteor':
            ra.livingmeteor(variables, rc[1][13:], rc[2])

        if rc[1][:14] == 'handofragnaros':
            variables[rc[3]] = ra.handofragnaros(rc[1][15:], rc[2])

print(variables)
