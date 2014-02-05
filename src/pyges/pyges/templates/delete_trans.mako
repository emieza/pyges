<style type="text/css">
	.dt_tbl_cel { border: 1px solid black; padding: 5px; } /* each cell */
</style>

<h1>Pyges: delete translation</h1>
<h3>description</h3>
<table>

		<tr><td class="dt_tbl_cel">
			<strong>Language: </strong>${langs[page.lang]}</div>
			<br />
			<strong>Title: </strong>${page.title}
			<br />
			<strong>Text: </strong>
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
