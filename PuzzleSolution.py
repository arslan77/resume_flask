

class PuzzleSolution:

    def __init__(self):
        pass

    def solve(self, str):
        matrix = self.parse(str)
        matrix = self.populate_missing_relation(matrix)
        matrix = self.solve_2nd_part(matrix)
        return self.stringify(matrix)

    def stringify(self, matrix):
        return_str = " ABCD"
        char_number = 1
        for row in matrix:
            return_str+='\n'+return_str[char_number]
            for relation in row:
                return_str += relation
            char_number += 1
        return return_str
    def solve_2nd_part(self, matrix):
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == '-':
                    for k in range(len(matrix)):
                        if matrix[k][j] != '-' and k != j:
                            if matrix[k][i] != '-':
                                matrix[i][j] = self.inverse(matrix[k][i])
                                break
        return matrix


    def populate_missing_relation(self, matrix):
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if i == j and matrix[i][j] == '-':
                    matrix[i][j] = "="
                elif matrix[i][j] != '-' and matrix[j][i] == '-':
                    matrix[j][i] = self.inverse(matrix[i][j])
        return matrix

    def inverse(self, relation):
        if relation == '<':
            return '>'
        else:
            return '<'

    def parse(self, str):
        str = str.split(" ")
        str = str[4].split("\n")
        matrix = []
        for i in range(1, len(str)-1):
            line = str[i]
            row = []
            for j in range(1, len(line)):
                relation = line[j]
                row.append(relation)
            matrix.append(row)
        return matrix