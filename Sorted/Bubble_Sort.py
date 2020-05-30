
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


def compute(str):
    lst = ()
    count = 0
    for x in range(len(offices.items())):
        for i, j in offices.items():
            for k, v in tuple(j.items()):
                print(k, v)
                if str == v[1]:
                    print(k, v)
        break



        # for x in offices.keys():
        #     for j in offices.values():
        #         t = tuple(j.items())
        #         for k, v in t:
        #             k_list.append(k)
        #             v_list.append(v)
        #             print(k)
        #             # print(f'{k} ---> {v}')
        #         break
        #
        #     break

            # t = tuple(v.items())
            #
            # k_list.append(k)
            # v_list.append(v)
            #print(v)
            #print(f'{k}-{v}')



            # lst.append(t)
            # for j in sorted(lst):
            #     print(j)
            # for k, v in iter(j):
            #
            #     print(f'{k}===>{v}')

            # if str == j[1][1]:
            #     print(j)
            # if str == j[1][1]:
            #     print(j)
            # if str == j[1][1]:
            #     print(j)


if __name__ == '__main__':
    compute('Autodesk')

# for x in range(len(offices)):
#     for i, j in offices.items():
#         t = tuple(j.values())
#         if re.findall('VMware', t[1]):
#             print(i, t)
#     break