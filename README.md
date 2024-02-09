# FSubdomaiNM
# Sobre ℹ️
Este projeto foi concebido com o propósito de promover aprendizado. Seu objetivo principal é explorar o funcionamento das buscas de subdomínios, além de aprofundar o entendimento sobre os métodos empregados na criação de ferramentas para este fim específico. Ao mergulhar nesse processo, busca-se não apenas compreender os aspectos técnicos envolvidos, mas também cultivar habilidades práticas no desenvolvimento de soluções voltadas para a segurança e eficiência na gestão de domínios e subdomínios na internet.

# Instalação 🛠️
Install beautifulsoup4
`pip install beautifulsoup4`
Install dnspython
`pip install dnspython`
Install requests
`pip install requests`
Install urllib3
`pip install urllib3`

# Como Usar 🚀
Brute force
`python <site> -b <wordlist.txt>`
Web Scraping
`python <site> -w <Name_for_output.txt>`
Records Types
`python <site>`

# Métodos Usados 🛠️
Brute Force
O método de brute force para encontrar subdomínios é uma abordagem onde se faz uma tentativa sistemática de todas as combinações possíveis de subdomínios dentro de um domínio principal. Essa técnica geralmente é realizada através de scripts ou ferramentas automatizadas que geram uma lista de subdomínios com base em palavras-chave, dicionários pré-definidos ou até mesmo por meio da geração aleatória de strings.

Web Scraping
O método de Web Scraping para encontrar subdomínios envolve a extração de informações diretamente de páginas da web para identificar subdomínios relacionados a um domínio principal. Essa técnica é particularmente útil quando os subdomínios não estão diretamente expostos em registros DNS públicos ou quando se deseja obter uma lista mais abrangente e detalhada de subdomínios ativos.

Record Types
O método de Record Types Para encontrar subdomínios usando registros DNS, você pode seguir um processo que envolve consultas aos registros DNS do domínio principal. Embora consultar registros DNS seja uma técnica útil para encontrar subdomínios, ela pode não revelar todos os subdomínios existentes, especialmente se estiverem ocultos por medidas de segurança ou não estiverem diretamente configurados nos registros DNS públicos 

# Versão e Próximas Versões 🔄
Primeira versão v1.0

Objetivo das próximas versões é a correção de bugs e a implementação de novas técnicas.

# Complementos Finais 🎉
Este é o meu primeiro programa em Python, ainda há muitos bugs e logicas para aprender.
