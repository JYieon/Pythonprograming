import pandas as pd


class ClassificationExcel:

    def __init__(self, order_xlsx_filename, partner_info_xlsx_filename):
        # 주문목록
        df = pd.read_excel(order_xlsx_filename)
        df = df.rename(columns=df.iloc[1]) #1번줄에 있는 것을 변수로 삼아 rename
        df = df.drop([df.index[0], df.index[1]]) #0번, 1번줄 지움
        df = df.reset_index(drop=True) #좌측 인덱스 번호 재정리
        self.order_list = df

        # 파트너목록
        df_partners = pd.read_excel(partner_info_xlsx_filename)
        
        self.brands = df_partners['브랜드'].to_list()
        self.partners = df_partners['업체명'].to_list()

        # print(len(self.brands), self.brands)
        # print(len(self.partners), self.partners)
        # print(self.brands[0], self.partners[0])
        # print(self.order_list['상품명'].head())


if __name__ == '__main__':
    ce = ClassificationExcel('주문목록20221112.xlsx', '파트너목록.xlsx')
    ce.classify()
