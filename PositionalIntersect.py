def getDocId(p):
    return p[0]


def getPosition(p):
    return p[1]


def positionalIntersect(p1,p2,k):

    answer=[]                                                    # answer <- ()

    i=j=0
    while i<len(p1) and j<len(p2):                               # while (p1 != nil and p2 != nil)
        if getDocId(p1[i])==getDocId(p2[j]):                     # if docID(p1) = docID(p2)
            list=[]                                              # l <- ()
            pp1=getPosition(p1[i])                               # pp1 <- positions(p1)
            pp2=getPosition(p2[j])                               # pp2 <- positions(p2)

            #loop for indexing the lists
            x=y=0
            while x<len(pp1):                                    # while (pp1 != nil)
                while y<len(pp2):                                # while (pp2 != nil)
                    if abs(pp1[x]-pp2[y])<=k:                    # if |pos(pp1) − pos(pp2)| ≤ k
                        list.append(pp2[y])                      # ADD(l, pos(pp2))
                    elif pp2[y]>pp1[x]:                          # else if pos(pp2) > pos(pp1)
                        break
                    y+=1

                while len(list)>0 and abs(list[0]-pp1[x])>k:     # while l!=<> and |l[0] − pos(pp1)| > k
                    list.remove(list[0])                         # delete(l[0])
                for ps in list:                                  # for each ps in l
                    answer.append([getDocId(p1[i]),pp1[x],ps])   # ADD(answer, docID(p1), pos(pp1), ps)
                x+=1

            i+=1
            j+=1

        elif getDocId(p1[i])<getDocId(p2[j]):
            i+=1
        else:
            j+=1

    return answer



def test_bench():
        print("to be or not to be\n")
        to = [[1, [7, 18, 33, 72, 86, 231]], [2, [1, 17, 74, 222, 255]], [4, [8, 16, 190, 429, 433]], [5, [363, 367]],
              [7, [13, 23, 191]]]
        be = [[1, [17, 25]], [4, [17, 191, 291, 430, 434]], [5, [14, 19, 101]]]
        print("to: ", to)
        print()
        print("be: ", be)
        print()
        print(
        "Intersection result of \"to /1 be\": ", positionalIntersect(to, be, 1))
        print()
        print(
        "Intersection result of \"be /3 to\": ", positionalIntersect(be, to, 3))
        print()
        print(
        "Intersection result of \"to /5 be\": ", positionalIntersect(to, be, 5))

test_bench()