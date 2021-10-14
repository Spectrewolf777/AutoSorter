import os
import shutil

current_dir = os.getcwd()

for f in os.listdir(current_dir):
    filename,file_ext = os.path.splitext(f)
    print(file_ext)

    try:

        if not file_ext:

            pass



        elif file_ext in ('.png', '.jpg', '.jpeg'):
            
            print('found')
            x = 'Image Files'
            try:
                os.mkdir(x)

            except (FileExistsError ):
                pass

                
            
            old_location = current_dir + "\\" + filename + file_ext
            new_location = current_dir + "\\"+ x + "\\" + filename + file_ext
            print(old_location)
            print(new_location)
            shutil.move(old_location, new_location)
            print('Done')


        elif file_ext in ('.pdf'):
            
            
            print('found')
            x = 'PDF Files'
            try:
                os.mkdir(x)

            except (FileExistsError ):
                pass

                
            
            old_location = current_dir + "\\" + filename + file_ext
            new_location = current_dir + "\\"+ x + "\\" + filename + file_ext
            print(old_location)
            print(new_location)
            shutil.move(old_location, new_location)
            print('Done')


        elif file_ext in ('.mp3', '.wav', '.ogg'):
            
            
            print('found')
            x = 'Audio Files'
            try:
                os.mkdir(x)

            except (FileExistsError ):
                pass

                
            
            old_location = current_dir + "\\" + filename + file_ext
            new_location = current_dir + "\\"+ x + "\\" + filename + file_ext
            print(old_location)
            print(new_location)
            shutil.move(old_location, new_location)
            print('Done')



        elif file_ext in ('.zip', '.7z', '.rar'):
            
            
            
            print('found')
            x = 'Commpressed Files'
            try:
                os.mkdir(x)

            except (FileExistsError ):
                pass

                
            
            old_location = current_dir + "\\" + filename + file_ext
            new_location = current_dir + "\\"+ x + "\\" + filename + file_ext
            print(old_location)
            print(new_location)
            shutil.move(old_location, new_location)
            print('Done')
        




        elif file_ext in ('.mp4'):
            
            
            
            print('found')
            x = 'Video Files'
            try:
                os.mkdir(x)

            except (FileExistsError ):
                pass

                
            
            old_location = current_dir + "\\" + filename + file_ext
            new_location = current_dir + "\\"+ x + "\\" + filename + file_ext
            print(old_location)
            print(new_location)
            shutil.move(old_location, new_location)
            print('Done')

        elif file_ext in ('.py'):
            print("skip so code doesnt commit suicide")


        elif file_ext in ('.xls', '.xlsx', '.xltx', '.xlsm', '.mpx'):
            
            
            print('found')
            x = 'Excel Files'
            try:
                os.mkdir(x)

            except (FileExistsError ):
                pass

                
            
            old_location = current_dir + "\\" + filename + file_ext
            new_location = current_dir + "\\"+ x + "\\" + filename + file_ext
            print(old_location)
            print(new_location)
            shutil.move(old_location, new_location)
            print('Done')


        elif file_ext in ('.exe'):
            
                
            print('found')
            x = 'Executable Files'
            try:
                os.mkdir(x)

            except (FileExistsError ):
                pass

                
            
            old_location = current_dir + "\\" + filename + file_ext
            new_location = current_dir + "\\"+ x + "\\" + filename + file_ext
            print(old_location)
            print(new_location)
            shutil.move(old_location, new_location)
            print('Done')


        elif file_ext in ('.doc', '.docx'):
            
                
            print('found')
            x = 'Word Files'
            try:
                os.mkdir(x)

            except (FileExistsError ):
                pass

                
            
            old_location = current_dir + "\\" + filename + file_ext
            new_location = current_dir + "\\"+ x + "\\" + filename + file_ext
            print(old_location)
            print(new_location)
            shutil.move(old_location, new_location)
            print('Done')



        elif file_ext in ('.txt'):
            
                
            print('found')
            x = 'Text Files'
            try:
                os.mkdir(x)

            except (FileExistsError ):
                pass

                
            
            old_location = current_dir + "\\" + filename + file_ext
            new_location = current_dir + "\\"+ x + "\\" + filename + file_ext
            print(old_location)
            print(new_location)
            shutil.move(old_location, new_location)
            print('Done')


        elif file_ext in ('.STEP'):
            
                
            print('found')
            x = 'SolidWorks Files'
            try:
                os.mkdir(x)

            except (FileExistsError ):
                pass

                
            
            old_location = current_dir + "\\" + filename + file_ext
            new_location = current_dir + "\\"+ x + "\\" + filename + file_ext
            print(old_location)
            print(new_location)
            shutil.move(old_location, new_location)
            print('Done')


        elif file_ext in ('.msi'):
            
                
            print('found')
            x = 'Windows installer Files'
            try:
                os.mkdir(x)

            except (FileExistsError ):
                pass

                
            
            old_location = current_dir + "\\" + filename + file_ext
            new_location = current_dir + "\\"+ x + "\\" + filename + file_ext
            print(old_location)
            print(new_location)
            shutil.move(old_location, new_location)
            print('Done')


        


        elif file_ext in ('.blend', '.fbx'):
            
                
            print('found')
            x = '3D Files'
            try:
                os.mkdir(x)

            except (FileExistsError ):
                pass

                
            
            old_location = current_dir + "\\" + filename + file_ext
            new_location = current_dir + "\\"+ x + "\\" + filename + file_ext
            print(old_location)
            print(new_location)
            shutil.move(old_location, new_location)
            print('Done')

        elif file_ext in ('.slx'):
            
                
            print('found')
            x = 'MatLabOrSimulink Files'
            try:
                os.mkdir(x)

            except (FileExistsError ):
                pass

                
            
            old_location = current_dir + "\\" + filename + file_ext
            new_location = current_dir + "\\"+ x + "\\" + filename + file_ext
            print(old_location)
            print(new_location)
            shutil.move(old_location, new_location)
            print('Done')


        elif file_ext in ('.kra'):
            
                
            print('found')
            x = 'Krita Files'
            try:
                os.mkdir(x)

            except (FileExistsError ):
                pass

                
            
            old_location = current_dir + "\\" + filename + file_ext
            new_location = current_dir + "\\"+ x + "\\" + filename + file_ext
            print(old_location)
            print(new_location)
            shutil.move(old_location, new_location)
            print('Done')



        


        
    


        






     

    except (FileNotFoundError, PermissionError):
        pass
