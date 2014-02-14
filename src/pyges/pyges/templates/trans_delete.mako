<!-- TRANSLATE -->

<style type="text/css">
	.dt_tbl_cel { border: 1px solid black; padding: 5px; } /* each cell */
</style>

<h1>Pyges: delete translation</h1>
<h3>description</h3>
<table>
	% for page in pages:
		<tr><td class="dt_tbl_cel">
			<strong>Language: </strong>${langs[page.lang]}</div>
			<br />
			<strong>Title: </strong>${page.title}
			<br />
			<strong>Text: </strong>
			<div>${page.text}</div>
		</td></tr>
	% endfor
</table>
<br />
<form method="post">
	<input type="text" name="fn" value="${fn}" style="display:none;"/>
	<input type="text" name="id" value="${id}" style="display:none;"/>
	<input type="checkbox" name="confirm" value="ok"/> Delete confimation
	<br /><br />
	<input type="submit" value="Send">
</form>

<a href="/trans_menu">Return menu translations</a>
<br />
<a href="/">Return home</a>

<!--  -->