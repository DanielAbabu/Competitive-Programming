class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for r in range(len(image)):
            image[r].reverse()
            for c in range(len(image[0])):
                image[r][c]= abs(image[r][c]-1)


        return image

