class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        totalDist = sum(travel)
        # Indexing for distTravel [M, P, G]
        found = {'M': False, 'P':False, 'G':False}
        distTravel = [totalDist] * 3
        counter = 0 

        counter += len(''.join(garbage))
        index = len(garbage)-1
        while (index >= 1 and totalDist in distTravel):
            if('M' not in garbage[index] and not found['M']):
                distTravel[0] -= travel[index-1]
            elif('M' in garbage[index]):
                found['M'] = True

            if('P' not in garbage[index] and not found['P']):
                distTravel[1] -= travel[index-1]  
            elif('P' in garbage[index]):
                found['P'] = True

            if('G' not in garbage[index] and not found['G']):
                distTravel[2] -= travel[index-1]
            elif('G' in garbage[index]):
                found['G'] = True

            index -= 1

        counter += sum(distTravel)
        return counter
                    # for i in range(len(garbage)):
        #     for j in (garbage[i]):
        #         if(j=='M'):
