
offices = {
    "id1": {
        "$oid": "5d336c36a6e07114ac728cc2",
        "title": "Autodesk",
        "startDt" : "2020-06-07T11"
    },
    "id2": {
        "$oid": "5d336c36a6e07114ac728cc4",
        "title": "Citrix",
        "startDt": "2020-04-07T11"
    },
    "id3": {
        "$oid": "5d336c36a6e07114ac728cc2",
        "title": "Autodesk",
        "startDt": "2020-03-07T11"
    },
    "id4": {
        "$oid": "5d336c36a6e07114ac728cc3",
        "title": "VMware",
        "startDt": "2020-11-07T11"
    }

}


def compute():
    st = input('Enter title name: ')
    for x in range(len(offices.items())):
        for i, j in offices.items():
            t = tuple(j.items())
            if st == t[1][1]:
                print(f'{t[1][0]}: {st} ===> {t[2][0]} : {t[2][1]}')

        break






            # if st == t[1][1]:
            #     print(f'{t[1][0]}: {st} ===> {t[2][0]} : {t[2][1]}')




            # if st == t[1][1]:
            #     print()



            # if st != t[1][1]:
            #     print(f'{t[1][0]}: {st} ===> {t[2][0]} : {t[2][1]}')




if __name__ == '__main__':
    compute()

    # k_list = []
    # v_list = []
    # for x in range(len(offices.items())):
    #     for i, j in offices.items():
    #         for k, v in tuple(j.items()):
    #             k_list.append(k)
    #             v_list.append(v)
    #             if str == v[1]:
    #                 print(str, v_list[0],v_list[2])
    #                 print(f'{k_list[1]}:{str} ====> {k_list[0]} = {v_list[0]}, {k_list[2]} = {v_list[2]}')
    #             break
    #     break
    #

