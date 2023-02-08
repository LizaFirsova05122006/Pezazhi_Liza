from flask import Flask, url_for, request

app = Flask(__name__)


@app.route('/carousel', methods=['POST', 'GET'])
def astronaut_selection():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                            <title>Фирсова Елизавета</title>
                          </head>
                          <body>
                            <div>
                            <h1 align="center">Фирсова Елизавета</h1>
                            <h3 align="center">вся жизнь в фото</h3>
                            <h5>Больше фотографий:</h5>
                            <a href="https://vk.com/lizavetka0512">Фирсова Елизавета<a>
                            </div>
                            <div id="myCarousel" class="carousel slide" data-ride="carousel">
                                <ol class="carousel-indicators">
                                    <li data-target="#myCarousel" data-slide-to="0" class="active"></li>
                                    <li data-target="#myCarousel" data-slide-to="1"></li>
                                    <li data-target="#myCarousel" data-slide-to="2"></li>
                                    <li data-target="#myCarousel" data-slide-to="3"></li>
                                    <li data-target="#myCarousel" data-slide-to="4"></li>
                                    <li data-target="#myCarousel" data-slide-to="5"></li>
                                    <li data-target="#myCarousel" data-slide-to="6"></li>
                                    <li data-target="#myCarousel" data-slide-to="7"></li>
                                    <li data-target="#myCarousel" data-slide-to="8"></li>
                                    <li data-target="#myCarousel" data-slide-to="9"></li>
                                    <li data-target="#myCarousel" data-slide-to="10"></li>
                                    <li data-target="#myCarousel" data-slide-to="11"></li>
                                    <li data-target="#myCarousel" data-slide-to="12"></li>
                                    <li data-target="#myCarousel" data-slide-to="13"></li>
                                    <li data-target="#myCarousel" data-slide-to="14"></li>
                                    <li data-target="#myCarousel" data-slide-to="15"></li>
                                    <li data-target="#myCarousel" data-slide-to="16"></li>
                                    <li data-target="#myCarousel" data-slide-to="17"></li>
                                    <li data-target="#myCarousel" data-slide-to="18"></li>
                                    <li data-target="#myCarousel" data-slide-to="19"></li>
                                </ol>
                                <div class="carousel-inner">
                                    <div class="item active">
                                        <img src="{url_for('static', filename='img/0.png')}" alt="First Slide">
                                    </div>
                                    <div class="item">
                                        <img src="{url_for('static', filename='img/1.png')}" alt="Second Slide">
                                    </div>
                                    <div class="item">
                                        <img src="{url_for('static', filename='img/2.png')}" alt="Third Slide">
                                    </div>
                                    <div class="item">
                                        <img src="{url_for('static', filename='img/3.png')}" alt="Fourth Slide">
                                    </div>
                                    <div class="item">
                                        <img src="{url_for('static', filename='img/4.png')}" alt="Fifth Slide">
                                    </div>
                                    <div class="item">
                                        <img src="{url_for('static', filename='img/8.png')}" alt="Sixth Slide">
                                    </div>
                                    <div class="item">
                                        <img src="{url_for('static', filename='img/9.png')}" alt="Seventh Slide">
                                    </div>
                                    <div class="item">
                                        <img src="{url_for('static', filename='img/10.png')}" alt="Eighth Slide">
                                    </div>
                                    <div class="item">
                                        <img src="{url_for('static', filename='img/5.png')}" alt="Ninth Slide">
                                    </div>
                                    <div class="item">
                                        <img src="{url_for('static', filename='img/6.png')}" alt="Tenth Slide">
                                    </div>
                                    <div class="item">
                                        <img src="{url_for('static', filename='img/7.png')}" alt="Eleventh Slide">
                                    </div>
                                    <div class="item">
                                        <img src="{url_for('static', filename='img/13.png')}" alt="Twelfth Slide">
                                    </div>
                                    <div class="item">
                                        <img src="{url_for('static', filename='img/14.png')}" alt="Thirteenth Slide">
                                    </div>
                                    <div class="item">
                                        <img src="{url_for('static', filename='img/15.png')}" alt="Fourteenth Slide">
                                    </div>
                                    <div class="item">
                                        <img src="{url_for('static', filename='img/12.png')}" alt="Fifteenth Slide">
                                    </div>
                                    <div class="item">
                                        <img src="{url_for('static', filename='img/16.png')}" alt="Sixteenth Slide">
                                    </div>
                                    <div class="item">
                                        <img src="{url_for('static', filename='img/17.png')}" alt="Seventeenth Slide">
                                    </div>
                                    <div class="item">
                                        <img src="{url_for('static', filename='img/18.png')}" alt="Eighteenth Slide">
                                    </div>
                                    <div class="item">
                                        <img src="{url_for('static', filename='img/19.png')}" alt="Nineteenth Slide">
                                    </div>
                                    <div class="item">
                                        <img src="{url_for('static', filename='img/20.png')}" alt="Twentieth Slide">
                                    </div>
                                </div>
                                <a class="carousel-control-prev" href="#carousel" role="button" data-slide="prev">
                                  <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                                  <span class="sr-only">Назад</span>
                                </a>
                                <a class="carousel-control-next" href="#carousel" role="button" data-slide="next">
                                  <span class="carousel-control-next-icon" aria-hidden="true"></span>
                                  <span class="sr-only">Вперёд</span>
                                </a>
                            </div>
                          </body>
                        </html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')