class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:

        tasks.sort(reverse=True)
        processorTime.sort()
        ans=0     
        j=0
        for i in range(len(processorTime)):
            ans=max(ans,processorTime[i]+tasks[j],processorTime[i]+tasks[j+1],processorTime[i]+tasks[j+2],processorTime[i]+tasks[j+3])
            j+=4
        return ans


        
        