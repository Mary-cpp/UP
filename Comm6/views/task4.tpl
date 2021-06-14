% rebase('layout.tpl', title=title, year=year, title2=title2, coefficients=coefficients, determinism=determinism, row=row, x=x,y=y)

<h2>{{ title }}.</h2>
<p><a class="btn btn-default" href="https://docs.google.com/document/d/1V9VP9P3X5Hr-4OKJXKHSBmKlt-n7I3ZjrouDd_v0vUc/edit?usp=sharing">Go to theory &raquo;</a></p>
<h3>{{ message }}</h3>

<img src="static/images/Task4text.PNG">

<h3> {{ title2 }}. </h3>
<form action="/time_series" method="post">
        <p><input type="text" size="50" name="X" placeholder="Y"></p>
        <p><input type="text" size="50" name="Y" placeholder="Y"></p>
        <p><input type="submit" value="Send"></p>
        <p><class="btn btn-default" input type="submit" value="Send"></p>
</form>
    