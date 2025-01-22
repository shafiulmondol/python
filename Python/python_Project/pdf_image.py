from pdf2image import convert_from_path
oldpdf=convert_from_path('download.pdf', poppler_path=r'D:\SHAFIUL MONDOL\Python\python_Project\poppler-24.07.0\Library\bin')
for i in range(len(oldpdf)):
    oldpdf[i].save("new"+str(i)+'.jpg','JPEG')