import requests,os
from random import randint


links = []
mp4_links = []
real_links = []
savedpage = 'Info.txt'
downloadpage = 'DownloadPage.txt'


#########Get Available Video List###########

def get_Videos_List():
    global links
    global real_links
    global mp4_links
    videos_link = 'https://archive.org/details/classic_tv_commercials_emperor?&sort=-week&page={}'.format(randint(1,70))
    go_to_link = requests.get(videos_link)
    
    ##############navigating to site to save page############
   
    with open(savedpage,'a+' , encoding = "utf-8") as page:page.write(go_to_link.text)     
    #############finding and saving div classes with video titles#######
    with open(savedpage,'r' ,encoding = "utf-8") as find_links:
        for line in find_links.readlines():
          if line.strip().startswith('<div class="item-ia" data-id=') and  line.strip() not in links:
              links.append(line.strip())
              
    ###########splitting class to get title#########################
    random_class = links[randint(1,len(links))].split('"')[3]
    links.clear()
    links.append(random_class)
    print(links)
    download_url = 'https://archive.org/download/' + links[0].strip()
    
    ########getting mp4link for url from list ###########
    with open(downloadpage,'a+',encoding = "utf-8") as page:
        go_to_url = requests.get(download_url)
        page.write(go_to_url.text)
    with open(downloadpage, 'r') as page:
        for line in page.readlines():
            if '.mp4' in line.strip():
                mp4_links.append(line)
    try:
        real_links.append(download_url+'/'+mp4_links[0].split('"')[1])
    except IndexError:
        with open(downloadpage, 'a+') as page:
         with open(savedpage,'a+') as page1:
            page.truncate(0)
            page1.truncate(0)

        videos_link = 'https://archive.org/details/classic_tv_commercials_emperor?&sort=-week&page={}'.format(randint(1,75))
        go_to_link = requests.get(videos_link)
        
        ##############navigating to site to save page############
        with open(savedpage,'a+' , encoding = "utf-8") as page:page.write(go_to_link.text)     
        
        #############finding and saving div classes with video titles#######
        with open(savedpage,'r' ,encoding = "utf-8") as find_links:
            for line in find_links.readlines():
              if line.strip().startswith('<div class="item-ia" data-id=') and  line.strip() not in links:
                  links.append(line.strip())
                  
        ###########splitting class to get title#########################
        random_class = links[randint(1,len(links))].split('"')[3]
        links.clear()
        links.append(random_class)
        print(links)
        download_url = 'https://archive.org/download/' + links[0].strip()
        
        ########getting mp4link for url from list ###########
        with open(downloadpage,'a+',encoding = "utf-8") as page:
            go_to_url = requests.get(download_url)
            page.write(go_to_url.text)
            
        with open(downloadpage, 'r') as page:
            for line in page.readlines():
                if '.mp4' in line.strip():
                    mp4_links.append(line)
    


    with open(downloadpage, 'a+') as page:
        with open(savedpage,'a+') as page1:
            page.truncate(0)
            page1.truncate(0)


def download_video():
    try:
        dir = os.makedirs('Videos')
        dir = r'Videos'
    except:
        dir = r'Videos'

    ###### getting video name#########
    file_name = real_links[0].split('/')[-1]
    print('Downloading {}'.format(file_name))

    ##### creating download request#####
    r = requests.get(real_links[0], stream=True)
    #####starting download#############
    with open(os.path.join(dir,file_name),"wb") as file:
        for chunk in r.iter_content(chunk_size=1024*1024):
            if chunk:
                file.write(chunk)
    print('Downloaded {}'.format(file_name))
    

def run_func():
    get_Videos_List()
    download_video()
