""""""

"""1. 导包"""
import pandas




class Operate_excel():

    def __init__(self,file_path):
        """打开表格"""
        self.table = pandas.read_excel(file_path)

    def get_data(self):
        data = []
        for i in self.table.index.values:
            data_dict = self.table.loc[i].to_dict()
            data.append(data_dict)
        return data


if __name__ == '__main__':
    opr = Operate_excel()
    data = opr.get_data()
    print(data)
