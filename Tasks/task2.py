# Task 2:
#    Write a program to read a csv using readlines() and insert each row to mongo db the first row of CSV will be the column headed

from pymongo import MongoClient

def fetchCSV(fileName):
  try:
    with open(fileName) as fp:
      table = []
      i = 0
      for row in fp:
        cols = row.split(',')
        tempRow = []
        for cell in cols:
          cell = cell.strip()
          tempRow.append(cell)
        table.append(tempRow)
    return table

  except Exception as e:
    print('Error in Fetch CSV : ', e)
    return False

def mongoJson(inpList):
  opList = []
  for i in range(1, len(inpList)):
    tempRow = {}
    for j in range(len(inpList[0])):
      tempRow[inpList[0][j]] = inpList[i][j]
    opList.append(tempRow)
  return opList

def connectCollection(Database1, colOpt):
  try:
    if colOpt == '1':
      collection = Database1.Students
    elif colOpt == '2':
      collection = Database1.Exams
    return collection

  except Exception as e:
    print('Error in Connect Collection : ', e)
    return False


# Main Module....

client = MongoClient(f'''mongodb+srv://Rahman:rahman12345@rahmanmaroonintern.lmf10.mongodb.net/myFirstDatabase?retryWrites=true&w=majority''')
Database1 = client.Database1
colOpt = input('Please choose the Collection Students(1)/ Exams(2) : ')
collection = connectCollection(Database1, colOpt)
fileName = input('Please enter the CSV file name (without Extension) : ')
myList = mongoJson(fetchCSV(fileName+'.csv'))

for doc in myList:
  returnVal = collection.insert_one(doc)