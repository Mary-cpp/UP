% rebase('layout.tpl', title=title, year=year, title2=title2, output = output)

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

<div class="output">
% if output:
% x = [*output[0]]
% y = [*output[1]]
% lvlX = [*output[2]]
% lvlY = [*output[3]]

<table border = "2">
    <tbody>
        <tr>
            <th>X</th>
            <th>Y</th>
        </tr>
        %size = len(x)
        %for r in range(size):
        <tr>
            <td>{{x[r]}}</td>
            <td>{{y[r]}}</td>
        </tr>
        %end
    </tbody>
    </table>
</div>

<h4>Average row X level<h4>
<p>lvlX</p>

<h4>Average row Y level<h4>
<p>lvlY</p>

