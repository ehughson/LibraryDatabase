import sqlite3
conn = sqlite3.connect('library.db')

cursor = conn.cursor()
cur = conn.cursor()
print("opened database successfully \n")
def main():
	with conn:
		cur = conn.cursor()
		print("Hello and Welcome to E&T Library Management System")

		response1 = input("do you have an account with us? ")

		if(response1.lower() == "no"):
			print("we can create a account quick, we just need some information from you!")
			lID = input("Lets create a unique ID for you, please enter a 6 (or more) digit number:")
			myQuery = "SELECT LibID FROM Members WHERE LibID= ? "
			cur.execute(myQuery, (lID, ))
			rows = cur.fetchall()
			if rows:
				print("this lib ID already exists, please start again!")
				return
			fName = input("what is your first name? ")
			lName = input("what is your last name? ")
			libAddress = "Surrey Libraries - Port Kells Branch"
			try:
				cur.execute("insert into Members(LibID, firstName, lastName, memberOfLib) values (?, ?, ?, ?)",
		            (lID, fName , lName, libAddress ))
				conn.commit()
			except sqlite3.IntegrityError:

				print("Error: There was a problem borrowing")
			
				
		
		response = input("would you like help from a librarian?")
		if(response.lower() == "yes"):
			myQuery = "SELECT firstName, lastName FROM Personnel WHERE position = 'Librarian'"
			
			cur.execute(myQuery)
			rows = cur.fetchall()
			if rows:
				print("the following are the available librarians who can help: ")
			else:
				print("error")

			for row in rows: 
				print(row)


			librarianFirst = input("which librarian would you like to help you? Please enter First Librarian: ")
			librarianLast = input(" Please enter librarian last name: ")
			myQuery = "SELECT pID FROM Personnel WHERE firstName = ? AND lastName = ?"
			cur.execute(myQuery, (librarianFirst, librarianLast, ))
			rows = cur.fetchall()
			if rows:
				print("We have the librarian here for you!")
			else:
				print("Sorry we dont have a librarian here by that name ")
				return

		
		
		#libraryid = input("what is your library ID? ")
	
			

		lookUp = input("Would you like to search for an item for you? (Yes/No)")
		if(lookUp.lower() == "yes"):
			lookup()


		borrow = input("Would you like to borrow an item from the library today?(Yes/No) ")
		if(borrow.lower() == "yes"):
			borrowItem()

		returnbook = input("Would you like to return an item ? (Yes/No)")
		if(returnbook.lower() == "yes" ):
			returnRecord()


		donating = input("would you like to donate to the library? (Yes/No)")
		if(donating.lower() == "yes"):
			donateRecord()
		

		EventLookUp = input("Would you like to look at the events we are holding? (Yes/No)")
		if(EventLookUp.lower() == "yes"):	
			findEvent()

		register= input("Would you like to register for an event? (Yes/No) ")
		if(register.lower() == "yes"):
			typeLU = "eventRegistration"
			registerEvent()

		volun = input("Would you like to volunteer? (Yes/No)")
		if(volun.lower() == "yes" ):	
			typeLU = "volunteering"
			volunteering()

		if conn:
			conn.commit()

	if conn:
		conn.close()
		print("Closed database successfully")


def lookup():	
	with conn:
		cur = conn.cursor()


		

		book = input("Are you searching for a book? (yes/no)")
		if(book.lower() == "yes"):
					itemISBN = input("Enter ISBN that you want to look up ")
					myQuery = "SELECT title FROM Book WHERE  ISBN =:item"
					cur.execute(myQuery, {"item":itemISBN})

					rows = cur.fetchall()
					if rows:
						title = rows[0]
						print("we do have the following book at the library {}".format(title)  )
					else:
						print("unfortunately we do not have a book in the library with " + itemISBN + " as a ISBN!\n")


					for row in rows:
						print(row)
					print("\n")
					return

		mag = input("Are you searching for a magazine? (yes/no)")
		if(mag.lower() == "yes"):
					itemISBN = input("Enter ISBN that you want to look up ")
					myQuery = "SELECT MagazineName FROM Magazine WHERE  ISBN =:item"
					cur.execute(myQuery, {"item":itemISBN})

					rows = cur.fetchall()
					if rows:
						title = rows[0]
						print("we do have the following Magazine at the library{}".format(title))
					else:
						print("unfortunately we do not have a Magazine in the library with " + itemISBN + "as a ISBN!\n")


					for row in rows:
						print(row)
					print("\n")
					return

		journal = input("Are you searching for a scientific journal? (yes/no)")
		if(journal.lower() == "yes"):
					itemISBN = input("Enter ISBN that you want to look up ")
					myQuery = "SELECT JournalName FROM ScientificJournal WHERE  ISBN =:item"
					cur.execute(myQuery, {"item":itemISBN})

					rows = cur.fetchall()
					if rows:
						title = rows[0]
						print("we do have the following Scientific Journal at the library {}".format(title))
					else:
						print("unfortunately we do not have a Scientific Journal in the library with " + itemISBN + "as a ISBN!\n")


					for row in rows:
						print(row)
					print("\n")
					return
		cd = input("Are you searching for a CD? (yes/no)")	
		if(cd.lower() == "yes"):
					itemISBN = input("Enter ISBN that you want to look up ")
					myQuery = "SELECT albumName FROM CD WHERE  ISBN =:item"
					cur.execute(myQuery, {"item":itemISBN})

					rows = cur.fetchall()
					if rows:
						title = rows[0]
						print("we do have the following CD at the library {}".format(title))
					else:
						print("unfortunately we do not have a CD in the library with " + itemISBN + "as a ISBN!\n")


					for row in rows:
						print(row)
					print("\n")
					return
		#finding an item in the library
		

		

		
def borrowItem():
	with conn:
		cur = conn.cursor()
		###############################################################################
		#borrow an item from the library

		book = input("Are you looking to borrow a book? (yes/no)")
		if(book.lower() == "yes"):
			ISBN = input("Enter ISBN that you want to borrow: ")
			myQuery = "SELECT Records.status FROM Records WHERE ISBN = ?"
			cur.execute(myQuery, (ISBN,  ))

		
			rows = cur.fetchall()
			if rows:
				print("we do have the following item at the library," + ISBN +": ")
			else:
				print("unfortunately we do not have the following item at the library" + ISBN  + "!\n")
			
			for row in rows:
				status = row[0]
				if(status.lower() == "unavailable"):
					print("sorry we dont have that book")
			
			myQuery = "SELECT title FROM Book WHERE ISBN = ?"
			cur.execute(myQuery, (ISBN,  ))	

			rows = cur.fetchall()
			
			for row in rows:
				ttl = row[0]
				response = input("is this the title of the book? {}".format(ttl))

			
			LibID = input("what is your library ID? ")
			IssueID = input("unique IssueID: ")
			IssueDate = input("todays date: " )
			DueDate = input("due date: ")

			try:
				cur.execute("insert into BorrowStatus(IssueID, ISBN, IssueDate, DueDate) values (?, ?, ?, ?)",
		            (IssueID, ISBN, IssueDate, DueDate))
				cur.execute("insert into Borrows(IssueID, ISBN,  borrowingID) values (?, ?, ?)",
		            (IssueID, ISBN, LibID))

			except sqlite3.IntegrityError:

				print("Error: There was a problem borrowing your book")
			if conn:
				conn.commit()
			return
		magazine = input("Are you looking to borrow a magazine? (yes/no)")
		if(magazine.lower() == "yes"):
			ISBN = input("Enter ISBN that you want to borrow: ")
			myQuery = "SELECT Records.status FROM Records WHERE ISBN = ?"
			cur.execute(myQuery, (ISBN,  ))

		
			rows = cur.fetchall()
			if rows:
				print("we do have the following item at the library," + ISBN +": ")
			else:
				print("unfortunately we do not have the following item at the library" + ISBN  + "!\n")
			
			for row in rows:
				status = row[0]
				if(status.lower() == "unavailable"):
					print("sorry we dont have that magazine")
			
			myQuery = "SELECT MagazineName FROM Magazine WHERE ISBN = ?"
			cur.execute(myQuery, (ISBN,  ))	

			rows = cur.fetchall()
			
			for row in rows:
				ttl = row[0]
				response = input("is this the name of the magazine? {}".format(ttl))

			
			LibID = input("what is your library ID? ")
			IssueID = input("unique IssueID: ")
			IssueDate = input("todays date: " )
			DueDate = input("due date: ")

			try:
				cur.execute("insert into BorrowStatus(IssueID, ISBN, IssueDate, DueDate) values (?, ?, ?, ?)",
		            (IssueID, ISBN, IssueDate, DueDate))
				cur.execute("insert into Borrows(IssueID, ISBN,  borrowingID) values (?, ?, ?)",
		            (IssueID, ISBN, LibID))

			except sqlite3.IntegrityError:

				print("Error: There was a problem borrowing")
			if conn:
				conn.commit()
			return
		journal = input("Are you looking to borrow a scientific journal ? (yes/no)")
		if(journal.lower() == "yes"):
			ISBN = input("Enter ISBN that you want to borrow: ")
			myQuery = "SELECT Records.status FROM Records WHERE ISBN = ?"
			cur.execute(myQuery, (ISBN,  ))

		
			rows = cur.fetchall()
			if rows:
				print("we do have the following item at the library," + ISBN +": ")
			else:
				print("unfortunately we do not have the following item at the library" + ISBN  + "!\n")
			
			for row in rows:
				status = row[0]
				if(status.lower() == "unavailable"):
					print("sorry we dont have that magazine")
			
			myQuery = "SELECT JournalName FROM ScientificJournal WHERE ISBN = ?"
			cur.execute(myQuery, (ISBN,  ))	

			rows = cur.fetchall()
			
			for row in rows:
				ttl = row[0]
				response = input("is this the name of the Scientific Journal? {}".format(ttl))

			
			LibID = input("what is your library ID? ")
			IssueID = input("unique IssueID: ")
			IssueDate = input("todays date: " )
			DueDate = input("due date: ")

			try:
				cur.execute("insert into BorrowStatus(IssueID, ISBN, IssueDate, DueDate) values (?, ?, ?, ?)",
		            (IssueID, ISBN, IssueDate, DueDate))
				cur.execute("insert into Borrows(IssueID, ISBN,  borrowingID) values (?, ?, ?)",
		            (IssueID, ISBN, LibID))

			except sqlite3.IntegrityError:

				print("Error: There was a problem borrowing")
			if conn:
				conn.commit()
			return
		cd= input("Are you looking to borrow a cd ? (yes/no)")
		if(cd.lower() == "yes"):
			ISBN = input("Enter ISBN that you want to borrow: ")
			myQuery = "SELECT Records.status FROM Records WHERE ISBN = ?"
			cur.execute(myQuery, (ISBN,  ))

		
			rows = cur.fetchall()
			if rows:
				print("we do have the following item at the library," + ISBN +": ")
			else:
				print("unfortunately we do not have the following item at the library" + ISBN  + "!\n")
			
			for row in rows:
				status = row[0]
				if(status.lower() == "unavailable"):
					print("sorry we dont have that magazine")
			
			myQuery = "SELECT albumName FROM CD WHERE ISBN = ?"
			cur.execute(myQuery, (ISBN,  ))	

			rows = cur.fetchall()
			
			for row in rows:
				ttl = row[0]
				response = input("is this the name of the Album? {}".format(ttl))

			
			LibID = input("what is your library ID? ")
			IssueID = input("unique IssueID: ")
			IssueDate = input("todays date: " )
			DueDate = input("due date: ")

			try:
				cur.execute("insert into BorrowStatus(IssueID, ISBN, IssueDate, DueDate) values (?, ?, ?, ?)",
		            (IssueID, ISBN, IssueDate, DueDate))
				cur.execute("insert into Borrows(IssueID, ISBN,  borrowingID) values (?, ?, ?)",
		            (IssueID, ISBN, LibID))

			except sqlite3.IntegrityError:

				print("Error: There was a problem borrowing")
			if conn:
				conn.commit()
			return

		return


def returnRecord():
	with conn:
		cur = conn.cursor()
		###############################################################################
		#return a borrowed item
		#finding an item in the library
		itemISBN = input("Enter ISBN that you want to return: ")
		
		myQuery = "SELECT BorrowStatus.IssueID, BorrowStatus.DueDate, Members.firstName FROM BorrowStatus, Borrows, Members WHERE BorrowStatus.ISBN = ? AND Borrows.IssueID = BorrowStatus.IssueID AND Members.LibID = Borrows.borrowingID"

		cur.execute(myQuery, (itemISBN,  ))

		rows = cur.fetchall()

		for row in rows:
			print(row)
			dueDate = row[1]
			issue = row[0]
			print("\n")
			print("The book is being returned by:")
			print(row[2])
		print("\n")

		LibID = input("what is your libraryid: ")
		returnID = input("what is the unique returnID: ")
		returnedOn = input("todays date: ")

		myQuery2 = "SELECT SUM(julianday() - julianday(BorrowStatus.DueDate ))*0.50 AS Fine FROM BorrowStatus, Borrows, Members WHERE BorrowStatus.ISBN = ? AND Borrows.IssueID = BorrowStatus.IssueID AND Members.LibID = Borrows.borrowingID"
		
		cur.execute(myQuery2, (itemISBN,  ))
		
		rows = cur.fetchall()
		
		for row in rows:
			fineAmount = row[0]
			print(row[0])
		print("\n")
		
		try:
			cur.execute("insert into ReturnStatus(ReturnID, IssueID, ISBN, DueDate, returnedOn, fineAmount) values (?, ?, ?, ?, ?, ?)",
	            (returnID, issue, itemISBN, dueDate, returnedOn, fineAmount))
			cur.execute("insert into Returns(ReturnID, IssueID, ISBN, returningID) values (?, ?, ?, ?)",
	            (returnID, issue, itemISBN, LibID))
		except sqlite3.IntegrityError:
			print("Error: There was a problem borrowing your book")

	if conn:
		conn.commit()
	return

	###############################################################################
	#donate an item to the library
def donateRecord():
	with conn:
		cur = conn.cursor()
		response = input("Are you sure you still want to donate? (yes/no)")
		found = 0

		if(response.lower() == "yes"):
			print("thank you so much for the donation!")
			typeRecord = input("what type of record (options: Magazine, Book, CD or Scientific Journal): ")

			if(typeRecord.lower() == "book"):
				fiction = input("is your book fiction? (Yes/No) ")
				genre = input("what genre is your book? For example, is it a murder mystery? ")
				title2 = input("what is the title of the book? ")
				authorFirstName2 = input("what is the authors first name? ")
				authorLastName2 = input("what is the authors last name? ")
				publisher = input("what is the publisher? ")

				myQuery = "SELECT ISBN FROM Book WHERE title = ? AND authorFirstName= ? AND authorLastName =? "
				cur.execute(myQuery, (title2, authorFirstName2, authorLastName2))
				rows = cur.fetchall()

				if rows: 
					titlecheck = rows[0]
					cur.execute("UPDATE Records SET numCopies = numCopies + 1 WHERE ISBN = ? ", (titlecheck))
					return


				ISBN = input("unique ISBN number: ")
				myQuery = "SELECT ISBN FROM Book WHERE ISBN = ? "
				cur.execute(myQuery, (ISBN, ))
				rows = cur.fetchall()
				if rows:
					print("this ISBN already exists")
					return

				local = input(" What rack number will this book have? ")
				numCop = 1
				ifavailble = input("will this book be available right away? ")
				if(ifavailble.lower() == 'yes'):
					availableOn = input("what is todays date: ")
					status = 'available'
				else:
					availableOn = input("what date in the future will this book be made available? ")
					status = 'unavailable'

				libAdd = "Surrey Libraries - Port Kells Branch"
				try:
					cur.execute("insert into Book(fiction, genre, title, authorFirstName, authorLastName, publisher, ISBN) values (?, ?, ?, ?, ?, ?, ?)",
			            (fiction, genre, title2, authorFirstName2, authorLastName2, publisher, ISBN ))
					cur.execute("insert into Records(ISBN, locationNumber, numCopies, availableOn, status, recordType,LibraryAddress ) values (?,?, ?, ?, ?, ?, ?)",
			            (ISBN, local, numCop, availableOn, status, typeRecord, libAdd))

				except sqlite3.IntegrityError:
					print("Error: There was a problem donating your item")


			elif(typeRecord.lower() == "magazine"):
				issueNum = input("what is the issue Number? ")
				volumeNum = input("what is the volume Number? ")
				magName = input("what is the magazine name? ")
				genre = input("what is the genre of magazine? For example, is it a fashion magazine?")
				


				myQuery = "SELECT ISBN FROM Magazine WHERE IssueNumber = ? AND volumeNumber= ? AND MagazineName =? "
				cur.execute(myQuery, (issueNum ,volumeNum, magName))
				rows = cur.fetchall()


				if rows: 
					titlecheck = rows[0]
					cur.execute("UPDATE Records SET numCopies = numCopies + 1 WHERE ISBN = ? ", (titlecheck))
					return

				ISBN = input("unique ISBN number: ")

				myQuery = "SELECT ISBN FROM Magazine WHERE ISBN = ? "
				cur.execute(myQuery, (ISBN, ))
				rows = cur.fetchall()
				if rows:
					print("this ISBN already exists")
					return


				local = input(" What rack number will this magazine have? ")
				numCop = 1
				ifavailble = input("will this magazine be available right away? ")
				if(ifavailble.lower() == 'yes'):
					availableOn = input("what is todays date: ")
					status = 'available'
				else:
					availableOn = input("what date in the future will this magazine be made available? ")
					status = 'unavailable'
				libAdd = "Surrey Libraries - Port Kells Branch"

				
				try:
					cur.execute("insert into Magazine(ISBN, IssueNumber, VolumeNumber, MagazineName, genre) values (?, ?, ?, ?, ?)",
			            (ISBN, issueNum, volumeNum, magName,genre))
					cur.execute("insert into Records(ISBN, locationNumber, numCopies, availableOn, status, recordType, LibraryAddress) values (?, ?, ?, ?, ?, ?, ?)",
			            (ISBN, local, numCop, availableOn, status, typeRecord, libAdd ))		

				except sqlite3.IntegrityError:
					print("Error: There was a problem donating your item")


			elif(typeRecord.lower() == "scientific journal"):
				
				issueNum = input("what is the issue Number? ")
				volumeNum = input("what is the volume Number? ")
				journalName = input("what is the journal name? ")
				publisher = input("who is the publisher for the magazine? ")


				myQuery = "SELECT ISBN FROM ScientificJournal WHERE IssueNumber = ? AND volumeNumber= ? AND JournalName =? "
				cur.execute(myQuery, (issueNum ,volumeNum, journalName))
				rows = cur.fetchall()

				if rows:
					print(" we already have that item so we will add it to the collection ")
					titlecheck = rows[0]
					cur.execute("UPDATE Records SET numCopies = numCopies + 1 WHERE ISBN = ? ", (titlecheck))
					return


				ISBN = input("unique ISBN number: ")


				myQuery = "SELECT ISBN FROM ScientificJournal WHERE ISBN = ? "
				cur.execute(myQuery, (ISBN, ))
				rows = cur.fetchall()
				if rows:
					print("this ISBN already exists")
					return

				local = input(" What rack number will this magazine have? ")
				numCop = 1
				ifavailble = input("will this  Scientific Journal be available right away? ")
				if(ifavailble.lower() == 'yes'):
					availableOn = input("what is todays date: ")
					status = 'available'
				else:
					availableOn = input("what date in the future will this magazine be made available? ")
					status = 'unavailable'
				libAdd = "Surrey Libraries - Port Kells Branch"

				try:
					cur.execute("insert into ScientificJournal(ISBN, IssueNumber, volumeNumber, JournalName, publisher) values ( ?, ?, ?, ?, ?)",
					    (ISBN, issueNum, volumeNum, journalName, publisher))
					cur.execute("insert into Records(ISBN, locationNumber, numCopies, availableOn, status, recordType, LibraryAddress) values (?, ?, ?, ?, ?, ?, ?)",
					    (ISBN, local, numCop, availableOn, status, typeRecord, libAdd))	
				except sqlite3.IntegrityError:
					print("Error: There was a problem donating your item")
				

			elif(typeRecord.lower() == "cd"):
				
				
				artName = input("what is the artists's name? ")
				albName = input("what is the album name? ")
				recName = input("who is the recording company? ")
				numTracks = input("how many tracks do this cd contain? ")

				myQuery = "SELECT ISBN FROM CD WHERE artistName = ? AND albumName = ? AND RecordingCompany =? "
				cur.execute(myQuery, (artName, albName, recName ))
				rows = cur.fetchall()
				if rows:
					print(" we already have that item so we will add it to the collection ")
					isbn = rows[0]
					cur.execute("UPDATE Records SET numCopies = numCopies + 1 WHERE ISBN = ? ", (isbn))
					return


				ISBN = input("unique ISBN number: ")

				myQuery = "SELECT ISBN FROM CD WHERE ISBN = ? "
				cur.execute(myQuery, (ISBN, ))
				rows = cur.fetchall()
				if rows:
					print("this ISBN already exists")

				local = input(" What rack number will this CD have? ")
				numCop = 1
				ifavailble = input("will this CD be available right away? ")
				if(ifavailble.lower() == 'yes'):
					availableOn = input("what is todays date: ")
					status = 'available'
				else:
					availableOn = input("what date in the future will this magazine be made available? ")
					status = 'unavailable'

				libAdd = "Surrey Libraries - Port Kells Branch"
						
				try:
					cur.execute("insert into CD(ISBN, artistName, albumName, RecordingCompany, numTracks) values ( ?, ?, ?, ?, ?)",
					    (ISBN, artName, albName, recName, numTracks))
					cur.execute("insert into Records(ISBN, locationNumber, numCopies, availableOn, status, recordType, LibraryAddress) values (?, ?, ?, ?, ?, ?, ?)",
					    (ISBN, local, numCop, availableOn, status, typeRecord, libAdd))		
				except sqlite3.IntegrityError:
					print("Error: There was a problem donating your item")

	if conn:
		conn.commit()
	return
				



	###############################################################################
	#find an event in the library
def findEvent():
	with conn:
		cur = conn.cursor()
		eventid = input(" what is the ID of the event you are looking for? ")

		#finding an item in the library
		myQuery = "SELECT title, roomBooked FROM Event WHERE eventID = ?"

		cur.execute(myQuery, (eventid,))

		rows = cur.fetchall()
		if rows:
			title = rows[0]
			print("the following event matches the ID you gave us")

		else:
			print("unfortunately we do not have the following item at the library " + eventid + "!\n")


		for row in rows:
			title = row[0]
			room = row[1]
			print("the event with the id is called: {}".format(title) )
			print("the event is in room: {}".format(room))
		print("\n")

		return




	###############################################################################
	#register for an event in the library
def registerEvent():
	bc = input("are you looking to register for a Book Club? ")
	if(bc.lower() == "yes"):
		with conn:
			cur = conn.cursor()
			eventid = input("what is the id of the event you are looking to register for? ")
			libID = input("what is your library ID? ")

			try:
				cur.execute("insert into Attends(eventid, LibID) values (?, ?)",
		            (eventid, libID))
			

			except sqlite3.IntegrityError:

				print("Error: There was a problem borrowing your book")
		if conn:
			conn.commit()
	be = input("are you looking to register for a Book Event? ")
	if(be.lower() == "yes"):
		with conn:
			cur = conn.cursor()
			eventid = input(" what is the ID of the event you are looking to register for? ")
			libID = input("what is your library ID? ")


			try:
				cur.execute("insert into Attends(eventid, LibID) values (?, ?)",
		            (eventid, libID))
			

			except sqlite3.IntegrityError:

				print("Error: There was a problem borrowing your book")
		if conn:
			conn.commit()
	ash = input("are you looking to register for a Art Show? ")
	if(ash.lower() == "yes"):
		with conn:
			cur = conn.cursor()
			eventid = input(" what is the ID of the event you are looking to register for? ")
			libID = input("what is your library ID? ")


			try:
				cur.execute("insert into Attends(eventid, LibID) values (?, ?)",
		            (eventid, libID))
			

			except sqlite3.IntegrityError:

				print("Error: There was a problem borrowing your book")
		if conn:
			conn.commit()

	fc = input("are you looking to register for a Film Screening? ")
	if(fc.lower() == "yes"):
		with conn:
			cur = conn.cursor()
			eventid = input(" what is the ID of the event you are looking to register for? ")
			libID = input("what is your library ID? ")


			try:
				cur.execute("insert into Attends(eventid, LibID) values (?, ?)",
		            (eventid, libID))
			

			except sqlite3.IntegrityError:

				print("Error: There was a problem borrowing your book")
		if conn:
			conn.commit()

	ac = input("are you looking to register for a art class? ")
	if(ac.lower() == "yes"):
		with conn:
			cur = conn.cursor()
			eventid = input(" what is the ID of the event you are looking to register for? ")
			libID = input("what is your library ID? ")



			try:
				cur.execute("insert into Attends(eventid, LibID) values (?, ?)",
		            (eventid, libID))
			

			except sqlite3.IntegrityError:

				print("Error: There was a problem borrowing your book")
		if conn:
			conn.commit()
	return


	###############################################################################
	#volunteer for the library
def volunteering():
	with conn:
		cur = conn.cursor()
		volunteer = input("would you like to volunteer for the library: ")
		if(volunteer.lower() == "yes"):
			print("thank you so much for wanting to volunteer with us, we need a few things to get you started: \n")
			libID = input("what is your library ID? ")
			hours = input("how many hours would you like to volunteer for a week? ")
			firstName = input("what is your first name? ")
			lastName = input("what is your last name? ")

			myQuery = "SELECT pID FROM Personnel, Members WHERE  Personnel.firstName = ? AND  Personnel.lastName= ? AND Members.LibID =? "
			cur.execute(myQuery, (firstName, lastName, libID))
			rows = cur.fetchall()


			if rows: 
				titlecheck = rows[0]
				response = input("is this your pID {}? If so it looks like you already work for the library".format(titlecheck))
				if(response.lower() == "yes"):
					return

				


			pid = input("Create a unique personal id number: ")

			position = "volunteer"

			addr = input("what is the address of the library you want to volunteer for? ")
			try:
				cur.execute("insert into volunteer(pID, LibID, VolunteerHours) values (?, ?, ?)",
		            (pid, libID, hours))
				cur.execute("insert into Personnel(pID, position, firstName, lastName, worksForLib) values (?, ?, ?, ?, ?)",
		            (pid, position, firstName, lastName, addr))
			

			except sqlite3.IntegrityError:

				print("Error: There was a problem with your unique pID -- try again")
	if conn:
		conn.commit()
	return





	###############################################################################
	#ask for help from a librarian

if __name__ == "__main__":
	main()













