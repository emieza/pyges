<h1>Pyges: delete translation</h1>
<table>
	<tr><td>
		<div>Language: ${langs[page.lang]}</div>
		<br />
		<div>Name: ${page.title}</div>
		<br />
		<div>Text:</div>
		<div>${page.text}</div>
	</td></tr>
</table>
<br />
<form method="post">
	<input type="radio" name="confirm"/>Delete confimation
	<br />
	<input type="submit" value="Send">
</form>
<br>
<a href="/">Return home</a>.
