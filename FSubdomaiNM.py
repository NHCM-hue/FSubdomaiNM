from bs4 import BeautifulSoup
import dns.resolver  
import urllib.request, requests
import sys, os

COR_VERMELHA = '\033[91m'
COR_ROXA = '\033[95m'
COR_VERDE = '\033[92m'
COR_PADRAO = '\033[0m'
COR_AZUL = '\033[94m'

def clear_screen():
    if os.name == 'nt':  # Sistema Windows
        os.system('cls')
    else:  # Outros sistemas (Linux, macOS)
        os.system('clear')

def print_banner():
    banner = """
    

    █████▒ ██████  █    ██  ▄▄▄▄   ▓█████▄  ▒█████   ███▄ ▄███▓ ▄▄▄       ██▓ ███▄    █  ███▄ ▄███▓
    ▓██   ▒▒██    ▒  ██  ▓██▒▓█████▄ ▒██▀ ██▌▒██▒  ██▒▓██▒▀█▀ ██▒▒████▄    ▓██▒ ██ ▀█   █ ▓██▒▀█▀ ██▒
    ▒████ ░░ ▓██▄   ▓██  ▒██░▒██▒ ▄██░██   █▌▒██░  ██▒▓██    ▓██░▒██  ▀█▄  ▒██▒▓██  ▀█ ██▒▓██    ▓██░
    ░▓█▒  ░  ▒   ██▒▓▓█  ░██░▒██░█▀  ░▓█▄   ▌▒██   ██░▒██    ▒██ ░██▄▄▄▄██ ░██░▓██▒  ▐▌██▒▒██    ▒██ 
    ░▒█░   ▒██████▒▒▒▒█████▓ ░▓█  ▀█▓░▒████▓ ░ ████▓▒░▒██▒   ░██▒ ▓█   ▓██▒░██░▒██░   ▓██░▒██▒   ░██▒
    ▒ ░   ▒ ▒▓▒ ▒ ░░▒▓▒ ▒ ▒ ░▒▓███▀▒ ▒▒▓  ▒ ░ ▒░▒░▒░ ░ ▒░   ░  ░ ▒▒   ▓▒█░░▓  ░ ▒░   ▒ ▒ ░ ▒░   ░  ░
    ░     ░ ░▒  ░ ░░░▒░ ░ ░ ▒░▒   ░  ░ ▒  ▒   ░ ▒ ▒░ ░  ░      ░  ▒   ▒▒ ░ ▒ ░░ ░░   ░ ▒░░  ░      ░
    ░ ░   ░  ░  ░   ░░░ ░ ░  ░    ░  ░ ░  ░ ░ ░ ░ ▒  ░      ░     ░   ▒    ▒ ░   ░   ░ ░ ░      ░   
                ░     ░      ░         ░        ░ ░         ░         ░  ░ ░           ░        ░   
                                ░  ░                                                              

                                                                                                                
    Tag     example                                Description

    [-h]     python -h                                   Helpme
    [-b]     python <site> -b <wordlist.txt>             Use to find subdomain with Brute Force 
    [-w]     python <site> -w <Name_for_output.txt>      Use to find subdomain with links inside the website 
                                                                <folder path> use to list the output of data   
    [-r]     python <site>                               Use to find records types                                                                                                                                                         


    Choose an option

    [1] Brute Force
    [2] Web Scraping
    [3] Tipos de Registros DNS
    [4] Sair
    """
    print(COR_ROXA + banner + COR_PADRAO)      
    
def brute_force(url, lista):
    with open(lista) as subdomains:
        read_lines = subdomains.readlines()
    for test in read_lines:
        try:
            test = test.strip()
            url_test = f'http://{test}.{url}'
            requisicao = requests.get(url_test)
            if requisicao.status_code == 200:
                print(COR_VERDE + f'[+] Subdomain found!: {test}.{url}')
            else:
                print(COR_VERMELHA + f'[-] Subdomain not found or outher status code: {test}.{url} {requisicao.status_code}')
        except KeyboardInterrupt:
            print('[x] Erro: Program interrupt]')
            print(COR_PADRAO)
            quit()
        except requests.exceptions.RequestException as e:
            pass
        
def web_scraping(url, lista):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}

    domain = f'http://{url}'

    request = urllib.request.Request(domain, headers=headers)
    page = urllib.request.urlopen(request)  #consultar o site e retornar o HTML para page
    soup = BeautifulSoup(page, 'html5lib') #Transforma o HTML em Soup, necessario importação do html5lib
    aTag = soup.find_all('a')  #variavel aTag vai encontrar tudo que tiver em "a" no arquivo soup

    with open(lista, 'a') as arquivo:  #with open vai criar um arquivo onde vai aplicar(a) toda vez que executar o for
        try:
            for link in aTag:   #variavel link vai receber o filtro
                href = link.get('href')  #link representa o a tag HTML 'a', .get fala para retorna todo href presente nesse link              
                if href and href.startswith('http'):   #essa estrutura if vai validar se o href comecar com http, se sim ele fara uma requisição do link
                    requisição = requests.get(href)                   
                    if(requisição.status_code == 200):  #essa outra estrutura validara se o status da pagina estiver 200
                        print(COR_VERDE + "[+] Status code is 200 OK: ", href)  
                        arquivo.write(f"{href}\n")  #adiciona o link ao arquivo
                    else:
                        print(COR_VERMELHA + "[X] Erro: Status code Erro!")
        except KeyboardInterrupt:
            print(COR_PADRAO)
            quit()

        except Exception as e:
            print(f"[X] Erro: An erro ocurred while processing the file: {e}")
            print(COR_PADRAO)
            
def record_types(url):
    record_type = ['A', 'AAAA', 'CNAME', 'SOA', 'NS', 'MX', 'PTR']

    for type in record_type:
        try:
            answer = dns.resolver.resolve(url, type)
            for server in answer:
                print(COR_VERDE + f'{type}', server.to_text())
        except dns.resolver.NoAnswer:
            pass
        except dns.resolver.NXDOMAIN:
            print('[X] DNS query, you ussually only to provide the domain name')
            print(COR_PADRAO)
            quit()

def main_menu():
    if len(sys.argv) < 2:
        clear_screen()
        print_banner()
        print(COR_AZUL)
        choice = input(">> Type in the desired option: ")

        if (choice == '1'):
            try:
                url = input(COR_AZUL +">> Type the URL: ")
                lista = input(f">> Type the Wordlist: ")
                print(COR_PADRAO)
                brute_force(url, lista)

            except KeyboardInterrupt:
                quit()

            except FileNotFoundError:
                print(COR_VERMELHA + "[X] Erro: The file cannot be opened. Make sure the directory exists and has write permissions")
                quit()
            finally:
                print("Ending the function Web scraping")

        elif (choice == '2'):
            try:
                print('[@] No need "http" "https"')
                url = input(">> Type the URL: ")
                name_list = input('>> Type the Wordlist: ')
                print(COR_PADRAO)
                web_scraping(url, name_list)

            except KeyboardInterrupt:
                quit()

            except FileNotFoundError:
                print(COR_VERMELHA + "[X] Erro:The file cannot be opened. Make sure the directory exists and has write permissions.")
                quit()

        elif (choice == '3'):
            try:
                url = input("Type the URL: ")
                record_types(url)
                print(COR_PADRAO)

            except KeyboardInterrupt:
                print(COR_PADRAO)
                quit()

        else:
            print(COR_PADRAO)
            quit()
        sys.exit(1)
    
    url = sys.argv[1]
    comando = sys.argv[2]  

    if(comando == '-b'):
        lista = sys.argv[3]
        brute_force(url, lista)

    elif(comando == '-w'):
        lista = sys.argv[3]
        web_scraping(url, lista)

    elif(comando == '-r'):
        record_types(url)
        print(COR_PADRAO)
    
    elif(comando == '-h'):
        print_banner()


if __name__ == "__main__":
    main_menu()

    