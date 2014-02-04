<h1>Pyges: delete translation</h1>
<h3>description</h3>
<table border="1">

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
	<input type="checkbox" name="confirm" value="ok"/> Delete confimation
	<br /><br />
	<input type="submit" value="Send">
</form>

<a href="/view_trans">Return view translations</a>
