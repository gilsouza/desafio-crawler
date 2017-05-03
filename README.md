
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
        Output: crawlerbaseTest.csv
	$ python3 epocacosmeticoscrawlerTest.py
        Output: epocacosmeticoscrawlerTest.csv
    
# Execução do Script
    
    $ python3 main.py
        Output: epocacosmeticoscrawlerTest.csv

# Questões

#### Agora você tem de capturar dados de outros 100 sites. Quais seriam suas estratégias para escalar a aplicação?
Com a solução atual é necessário estender a classe CrawlerBase implementando os métodos que darão inteligência ao crawler 
para realizar o scraping para os 100 sites.
Para uma execução mais eficiente e escalável poderíamos adotar um modelo semelhante ao do JMeter, onde uma máquina "master"
enviaria e pediria para as máquinas "slaves" executarem os crawlers em uma fila, por exemplo. Tornando mais fácil o acréscimo de
máquinas e crawlers para execução de forma distribuída.

#### Alguns sites carregam o preço através de JavaScript. Como faria para capturar esse valor.
Podemos entender o funcionamento do JavaScript utilizado no site e replicar no Crawler.
No site ecpocacosmeticos.com.br, por exemplo, se faz uso de JavaScript para criar a url e realizar o bind do evento click no botão "MOSTRAR MAIS PRODUTOS" em uma página de "categoria", por exemplo perfumes (menu perfumes).
Se precisássemos realizar a paginação dos produtos nesta categoria, faríamos o parse do site para utilizar a url gerada pelo JavaScript para obter mais resultados de produtos. O trecho de código do site que pode ser extraído para a paginação, com número de páginas e toda a url com query string, é exibido logo abaixo:

```
// GET http://www.epocacosmeticos.com.br/perfumes
<script type='text/javascript'>
    var pagecount_21135593;
    $(document).ready(function () {
        pagecount_21135593 = 85;
        $('#PagerTop_21135593').pager({ pagenumber: 1, pagecount: pagecount_21135593, buttonClickCallback: PageClick_21135593 });
        $('#PagerBottom_21135593').pager({ pagenumber: 1, pagecount: pagecount_21135593, buttonClickCallback: PageClick_21135593 });
        if (window.location.hash != '') PageClick_21135593(window.location.hash.replace(/\#/, ''));
    });
    PageClick_21135593 = function(pageclickednumber) {
        window.location.hash = pageclickednumber;
        $('#ResultItems_21135593').load('/buscapagina?fq=C%3a%2f1000001%2f&PS=20&sl=ae17d111-2690-49d2-bb26-164b5236a7bf&cc=4&sm=0&PageNumber=' + pageclickednumber,
            function() {
                $('#PagerTop_21135593').pager({ pagenumber: pageclickednumber, pagecount: pagecount_21135593, buttonClickCallback: PageClick_21135593 });
                $('#PagerBottom_21135593').pager({ pagenumber: pageclickednumber, pagecount: pagecount_21135593, buttonClickCallback: PageClick_21135593 });
            bindQuickView();
        });
    }
</script>
```

Já os demais sites, com soluções mais complexas ou desconhecidas, podemos utilizar o PhantomJS.

#### Alguns sites podem bloquear a captura por interpretar seus acessos como um ataque DDOS. Como lidaria com essa situação?
Existem algumas medidas que poderiam ser adotas para mitigar o risco de detecção como um ataque deste gênero:

	- Aumento do intervalo de tempo entre as requisições;
	- Uso de proxies ou VPNs para distribuir a faixa de ips utilizados para os acessos;
	- Em alguns sites específicos, pode ser necessário imitar o comportamento humano ao realizar as requisições,
	  tornando as requisições o menos sintéticas possíveis.

Essas seriam medidas a serem utilizadas de forma combinada.

#### Um cliente liga reclamando que está fazendo muitos acessos ao seu site e aumentando seus custos com infra. Como resolveria esse problema?
Através de uma reunião de alinhamento das necessidades das duas partes, poderia ser solicitado um ambiente, uma janela de execução (data e horário)
ou outros meios de diminuir os gastos e possíveis problemas que possam ser gerados através do aumento da carga em seus servidores.





