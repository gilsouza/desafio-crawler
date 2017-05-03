
# desafio-crawler
Crawler que visita o site epocacosmeticos.com.br e salva um arquivo .csv os dados dos produtos encontrados.

# Dependências

    Python3 - versão testada: 3.5.2
    pip3
    beautifulsoup4-4.4.1
    requests-2.9.1
    
# Instalação - Linux Ubuntu
    
    $ sudo apt-get update -y && sudo apt-get install -y git python3 python3-pip
    $ git clone https://github.com/gilsouza/desafio-crawler.git
    $ cd desafio-crawler
    $ pip3 install -r requirements.txt

# Execução dos Testes

	$ python3 crawlerbaseTest.py
	$ python3 epocacosmeticoscrawlerTest.py
    
# Execução do Script
    
    $ python3 main.py

# Questões

#### Agora você tem de capturar dados de outros 100 sites. Quais seriam suas estratégias para escalar a aplicação?
Com a solução atual é necessário extender a classe CrawlerBase implementando os métodos que darão inteligência ao crawler 
para realizar o scraping para os 100 sites.
Para uma execução mais eficiênte e escalável poderiamos adotar um modelo semelhante ao do JMeter, onde uma máquina "master"
enviaria e pediria para as máquinas "slaves" executarem os crawlers em uma fila, por exemplo. Tornando mais fácil o acréscimo de
máquinas e crawlers para execução de forma distribuída.

#### Alguns sites carregam o preço através de JavaScript. Como faria para capturar esse valor.
Utilizaria o PhantomJS.

#### Alguns sites podem bloquear a captura por interpretar seus acessos como um ataque DDOS. Como lidaria com essa situação?
Existem algumas medidas que poderiam ser adotas para mitigar o risco de detecção como um ataque deste gênero:

	- Aumento do intervalo de tempo entre requests;
	- Uso de proxies ou VPNs para distribuir a faixa de ips utilizados para os acessos;
	- Em alguns sites específicos, pode ser necessário imitar o comportamento humano ao realizar as requisições,
	  tornando as requisições menos sintéticas possíveis;
	- Ou combinando com o cliente um ambiente, uma faixa de horário ou ips que possam realizar o livre acesso aos sites.

Essas seriam medidas a serem utilizadas de forma combinada. *Acredito que a medida mais importe é o aumento do intervalo de tempo entre requests.*

#### Um cliente liga reclamando que está fazendo muitos acessos ao seu site e aumentando seus custos com infra. Como resolveria esse problema?
Através de uma reunião de alinhamento das necessidades das duas partes, poderia ser solicitado um ambiente, uma janela de execução (data e horário)
ou outros meios de diminuir os gastos e possíveis problemas que possam ser gerados através do aumento da carga em seus servidores.





