# Data stuff (pandas snippets)

Select only columns starting from index 3 to the end.

    df_ata = df[df.columns[3:]]
    
   Apply someFunc to each cell of column colName

     df['colName'] = df['colName'].map(str).apply(someFunc)

Apply a short func (lambda) to a column/Series

    df[col] = df[col].astype(str).apply(lambda cell: "" if ";" in cell else cell)
    
A combo between lambda and someFunc

    df['col'] = df['col'].apply(lambda cell: somFunc(cell))

Convert a nested list to a simple list

    li_all =  sorted(list(set(itertools.chain(*li_nested))))

Create a pd.Series by adding columns

    series = df['col'].map(str) + '/' + df['anotherCol'].map(str)

Create a new dataframe from a Series or list

    newdf = pd.DataFrame({'colName': series_or_list })

Get individual sheets as df from excel file

    df = pd.ExcelFile(excel_path)
    df1 = df.parse('Sheet1', skiprows=2)
    df2 = df.parse('Sheet2', skiprows=2)

Open an excel file with xlwings

    wb = xlwings.Book(excel_path)

Select a sheet with xlwings

    wb.sheets['Sheet1'].activate()
    sht_obj = wb.sheets['Sheet1']

Get/Update the  data from sheet 

    for idx, value in someDict.items():
    	sht_obj.range('E{}'.format(i+4)).value = value #update 
    	value = sht_obj.range('E{}'.format(i+4)).value #get

Update xlwings sheet obj using a loop

    #colName is coreponding to 'AS' xl column  
    for ix, val in dict_with_idx_and_value.items():
        cell = '{}{}'.format("AS", str(ix))
        sht_obj.range(cell).value = val
        time.sleep(0.01)

Remove copy warning from pandas

    pd.options.mode.chained_assignment = None #SettingWithCopyWarning
Ignore regex warnings

    warnings.filterwarnings("ignore", 'This pattern has match groups')

Select a specific sheet from an excel file

    df = pd.read_excel(xl_path, skiprows=3, sheet_name="Sheet1")

Select only needed columns from a df

    df = df[['colName1', 'colName2, 'colName4']] 

Check cells from specific columns individually (iterate thru cells)

    for i in df.index.tolist():
        data1 = df.loc[i, "col1"] # get data 
        data2 = df.loc[i, "col2"]
        if data2 > data1:
            df.loc[i, "col1"] = data2 # set data 
            df.loc[i, "col2"] = data1

Group data by same values from a column 

    df_generator = df.groupby(["colName"])
    dfdict = {}
    for val_grouped, df_with_same_val_for_colName in df_generator:
        dfdict[val_grouped] = df_with_same_val_for_colName

Create a new df from series or list

    newdf = pd.DataFrame({})
    newdf["colName1"] = somedf["col"]    
    newdf["colName2"] = pd.Series(someList)

Concatenating a list with dfs by rows or by columns

    df = pd.concat(df_list, axis=0) # axis=1 for columns

Saving a df to excel

    df.to_excel("path/xl_name.xlsx", index=False)

List with punctuation marks

    PUNCTUATION = list('!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~\n')

Commun elements between 2 (or more) lists

    commun = list(set.intersection(set(li1), set(li2)))

Not commun elements between 2 (or more) lists

    difference = set.difference(set(li1), set(li2))

Read something from a file

    data = open("file_name.txt", "r").read().splitlines()

Write something to a file (.txt, .py etc)

    with open("file_name.txt", "w") as f:
        f.write("some text\n")

Get a list of files from a directory and filter it by extension

    files = os.listdir("someDir")
    fnames = [f for f in files if f.endswith(".xls")]

Replace some text with another text from a string

    someString.replace("me gusta",  "no me gusta") 

Search something in a string

    if re.search(someString, valueToSearch):
	    # do stuff 

Rename a column from a df

    columns = df.columns.tolist()
    idx = columns.index("oldName")
    columns[idx] = "newName"

Remove empty cells from a df

    df['colName'].dropna()

Sending an email with Python

    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    
    class Mail:
    """Sending an email with smtp library"""
    
    def  __init__(self, smtpaddr, smtpport):
	    self.smtpaddr = smtpaddr
	    self.smtpport = smtpport
	    
    def  check_mail_inputs(self, fromaddr, frompassword, toaddr, subject, body):
	    """All must be type string"""
	    inputs_mail = [fromaddr, frompassword, toaddr, subject, body]
	    for i in inputs_mail:
		    if  not  isinstance(i, str):
			    raise  Exception("Parameter must be string!")
    
    def  send_mail(self, fromaddr, frompassword, toaddr, subject, body):
	    """Send and email using standard smtp module"""
    
	    self.check_mail_inputs(fromaddr, frompassword, toaddr, subject, body)
	    msg = MIMEMultipart()
	    msg['From'] = fromaddr
	    msg['To'] = toaddr
	    msg['Subject'] = subject
	    msg.attach(MIMEText(body, 'plain'))
	    server = smtplib.SMTP(self.smtpaddr, self.smtpport)
	    server.ehlo()
	    server.starttls()
	    server.ehlo()
	    server.login(fromaddr, frompassword)
	    text = msg.as_string()
	    server.sendmail(fromaddr, toaddr, text)

Get a list of numbers, letters and punctuation

    upper =  list(string.ascii_uppercase)
    lower =  list(string.ascii_lowercase)
    numbers =  list(string.digits)
    punctuation_marks =  list(str(string.punctuation))

Read and write a .json file

    def read_json(filepath):
	    """Return a dict form a json file"""
	    with  open(filepath) as j:
		    adict = json.load(j)
	    return adict
    
    def write_json(somedict, filepath):
	    """Write dict to Json file"""
	    with  open(filepath, "w") as f:
		    json.dump(somedict, f)

Generate some ID

    def generate_id(len_id):
    	"""Generate a random series of chars upper/lower + numbers"""
    	custom_id = []
    	for _ in  range(len_id):
    			custom_id.append(random.choice(self.characters_list))
    			custom_id_result =  ''.join(custom_id)
    	return custom_id_result

Get current date in the format you need

    def  current_date(date_format='%Y-%m-%d'):
	    """Get current date in year-month-day format(default)"""
	    date = datetime.now().strftime(date_format)
	    return date


Wait for file to be saved on disk

    def wait_file_on_disk(save_path_file, timeout=900):
	   """Wait file to be saved in the path specified on disk"""  
	   wait_until = datetime.now() + timedelta(seconds=timeout)
	   while os.path.isfile(save_path_file) !=  True:
		   if wait_until < datetime.now(): 
			    raise ValueError("Timeout reached!")
		   time.sleep(1)

Get all files path from a given directory

	def get_files(root_path):
		"""Walk thru a start path and return a list of paths to files"""
		allfiles = []
		for root, _, files in os.walk(root_path):
			for f in files:
				path_tofile = os.path.join(root, f)
				allfiles.append(path_tofile)
		return allfiles

Copy a folder and it's contents to another folder

	def  copy_dirs(src, dst, symlinks=False, ignore=None):
		"""Copy dirs and it's items from src to dst"""

		if  not os.path.exists(dst):
			os.makedirs(dst)
		for item in os.listdir(src):
			s = os.path.join(src, item)
			d = os.path.join(dst, item)
			if os.path.isdir(s):
				copy_dirs(s, d, symlinks, ignore)
			else:
				if  not os.path.exists(d) or os.stat(s).st_mtime - os.stat(d).st_mtime >  1:
					shutil.copy2(s, d)


Delete folder and it's contents

    def delete_dirs(apath):
	    """Delete directory and all it's subfolders""" 
	    try:
		    shutil.rmtree(apath) #delete folders, subfolders and files
	    except:
		    shutil.rmtree(apath, ignore_errors=True) #delete files that are not opened
		    raise  Exception("Not all files were deleted from {}".format(apath))

Move a folder 

    shutil.move(src, dst)

Check if a folder exists

    os.path.isdir(folder_path)

Check if a file exists

    os.path.isfile(file_path)

List duplicates in a list

    seen =  set()
    seen_add = seen.add
    seen_twice =  set( x for x in seq if x in seen or seen_add(x) )

Get a list with unique values with order kept

    seen =  set()
    seen_add = seen.add
    unique_li = [x for x in seq if  not (x in seen or seen_add(x))]


Simple error log
  

    def write_traceback(err):
	    """Write the error on a error txt file show the traceback of the error"""
	    err_time =  str(datetime.now()) #'2011-05-03 17:45:35.177000'
	    tb_error_msg = traceback.format_exc()
	    errormessage =  "###########\n{}\nERROR:\n{}\n\nDetails:\n{}\n###########\n\n\n".format(err_time, err, tb_error_msg)
	    with open("ERRORS.txt", "a") as errfile:
		    errfile.write(errormessage)
	    return errormessage

    #use case
    try:
	    #some stuff
	 except Exception as err:
		 errmsg = write_traceback(err)
		 print(errmsg)

Merge pdf's with pymupdf

    def  mergePDF(pdf_path, save_path):
	    """Merge all pdfs from a folder in one big pdf file"""
	    pdfContainer = fitz.open()
	    folderName = save_path.split("Merged pdf files")	[-1].replace("\\", '_')    
	    pdfNamesli = os.listdir(pdf_path)
    
	    failedtoadd = []
	    for pdfName in pdfNamesli:
		    pdfPath = os.path.join(pdf_path, pdfName)
		    try:
			    pdf = fitz.open(pdfPath)
		    except Exception  as e:
			    print("Can't open pdf: ", pdfPath, "\nGot: ", str(e))
			    failedtoadd.append(pdfPath)
			    continue
		    try:
			    pdfContainer.insertPDF(pdf)
		    except Exception  as e:
			    print("Check if pdf is merged: ", pdfPath)
			    failedtoadd.append(pdfPath)
			    continue
		    savePath = os.path.join(save_path, str(folderName))
		    pdfContainer.save('{}.pdf'.format(savePath))
    
	    return failedtoadd

Copy folder tree (mirror a folder structure)

    def mirrorDirs(inputFolder):
	    """Mirror the input folder by creating the same folder structure in the output folder"""
	    output = inputFolder.replace('originalFolder', 'copiedFolder')
	    os.mkdir(output)
	    dirOriginalli = []
	    dirCopiedli = []
	    for dirpath, dirnames, filenames in os.walk(inputFolder): 
		    mirrorPath = dirpath.replace('originalFolder', 'copiedFolder')
		    for dname in dirnames:
			    dirRaw = os.path.join(dirpath, dname)
			    dirtoCreate = os.path.join(mirrorPath, dname)
	    try:
		    os.mkdir(dirtoCreate)
		    dirOriginalli.append(dirRaw)
		    dirCopiedli.append(dirtoCreate)
	    except:
		    raise ValueError("Can't create directory!")
	    
	    return dirOriginalli, dirCopiedli

Extract all pages from a pdf as png (try to get text too)

    import fitz # PyMuPDF
    #print(fitz.__doc__)
    doc = fitz.open('iso.pdf')
    nrof_pg = doc.pageCount
    print(nrof_pg)

    # get all pages as images
    for idx_pg in range(nrof_pg):
	    page = doc.loadPage(idx_pg)
	    asimg = page.getPixmap()
	    asimg.writePNG('test_{}.png'.format(idx_pg+1))\
	    
    # get text from all pages
    for idx_pg in  range(nrof_pg):
	    page = doc.loadPage(idx_pg)
	    txt = page.getText().encode("utf-8")
	    print(txt)
    
    doc.close()

Extract text from an image using tesseract

     
    import pytesseract    
    from  PIL  import Image
 
    img = Image.open('test.png', 'r')
    img = img.convert('LA') # greyscale
    #img.save("testrrr.png", "PNG")
    img = img.resize((img.size[0]*2, img.size[1]*2), Image.ANTIALIAS) # double the size
    img.save("testr.png", "PNG")
 
    img = Image.open('testr.png')
      
    #path to your tesseract exe you installed or extracted 
    pytesseract.pytesseract.tesseract_cmd =  "folder/tesseract.exe"
    
    result = pytesseract.image_to_string(img.convert('RGB'), lang='eng').encode("utf-8")
    
    print(result)

Setting a new index for a df

    df.set_index('colName, inplace=True)

Get df as nested lists

    nestedli = df.as_matrix()
    nestedli = [list(li) for li in nestedli]


Filter df by 'Value not found' and 'Left blank' (~ will not contain)

    dffiltered = df[~df[df.columns].isin(['Value not found']).any(1)]
    dfok = dffiltered[~dffiltered[dffiltered.columns].isin(['Left blank']).all(1)]

Converting Timestamp from Pandas to datetime from Python

    df['colName'] = pd.to_datetime(df['colName'])

Drop a list of indexes from a df

    df = df.drop(df.index[idx_todel])
    df.reset_index(drop=True, inplace=True)

Keep (~ don't keep) in a column the list of values given

    values = ['value_to_keep1', 'value_to_keep2']
    df = df[(~)df["colName"].str.contains('|'.join(action), na=False)]

Get a list of combinations

    combo =  list(itertools.combinations(some_list, number_of_combinations))

Setting a custom index and keeping only the non-duplicated index value

    df.set_index('colName', inplace=True)
    df = df[~df.index.duplicated(keep='first')]

Drop nan values or duplicates for a subset from a given df

    df["colName"].replace('', np.nan, inplace=True)
    df.dropna(subset=['colName'], inplace=True)
    df.drop_duplicates(subset=['colName'], keep='last', inplace=True)
    df.reset_index(drop=True, inplace=True)

Read a .csv file using pandas

    df = pd.read_csv("fname.csv", sep=";", low_memory=False)

Write to a .csv file using pandas

    df.to_csv("fileName.csv", sep=";", index=False)

Read a file in .csv format in chunks (if file is to big)

    chunk_size =  50000 # rows
    with  open(filePath, 'r', encoding='utf-8') as  file:
    	for df_chunk in pd.read_csv(file, chunksize=chunk_size, sep=csv_separator, engine='python'):
		    df_chunk.to_csv("filename.csv", sep=csv_separator, index=False)
		    del df_chunk

Create a dataframe from dict

    df = pd.DataFrame.from_dict(ams_dict, orient='index')
    df = df.transpose()

Write a dict to a .pickle file for later use

    pickle_out = open("fileName.pickle","wb")
    pickle.dump(someDict, pickle_out)
    pickle_out.close()

Read a .pickle file (has python objects saved in it)

    infile = open("fileName.pickle",'rb')
    someDict = pickle.load(infile)
    infile.close()

