from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    return HttpResponse(
        '''
        <head> What in id it </head>
        <title> HOME </title>
        <body> text
        </body>
    '''
        )


def about(request):
    return HttpResponse('''
    
        <head>About us</head>
        <title>About us </title>
            <h1>Страница о НАС </h1>
          
            <hr/>
                <h2>About me </h2>
                <hr/>
                <p> <b>Lets talk 'bout me </b>
                    <br/> yes
                </p>
                <p> <i> I'm nick </b> </i>
                
                
        ''')
def plot(request):
    return HttpResponse('''
<head> график </head>
<body>
           <h1>Проверка исправной гработы графика с Trading_View </h1>
           <p> <strong> just p text </strong> </p>
            <hr/>
           
                <!-- TradingView Widget BEGIN -->
                    <div class="tradingview-widget-container">
                    <div id="tradingview_b24d0"></div>
                    <div class="tradingview-widget-copyright"><a href="https://ru.tradingview.com/symbols/NASDAQ-AAPL/" rel="noopener" target="_blank"><span class="blue-text">График AAPL</span></a> от TradingView</div>
  <script type="text/javascript" src="https://s3.tradingview.com/tv.js"></script>
  <script type="text/javascript">
  new TradingView.widget(
  {
  "autosize": false,
  "symbol": "NASDAQ:AAPL",
  "interval": "D",
  "timezone": "Etc/UTC",
  "theme": "dark",
  "style": "1",
  "locale": "ru",
  "toolbar_bg": "#f1f3f6",
  "enable_publishing": false,
  "allow_symbol_change": true,
  "container_id": "tradingview_b24d0"
}
  );
  </script center = "left">
</div>
<!-- TradingView Widget END -->

        </body>
        ''')