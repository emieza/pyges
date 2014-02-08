<style type="text/css">
	.et_tbl_cel { border: 1px solid black; padding: 5px; } /* each cell */
</style>

<h1>Pyges: edit translation</h1>
<h3>description</h3>
<table><tr><td class="et_tbl_cel">
	<form method="post">
		<input type="text" name="id" value="${id}" style="display:none;"/>
		<strong>Language: </strong>${langs[page.lang]}
		<br /><br />
		<strong>Title: </strong><input type="text" name="title" value="${page.title}"/>
		<br /><br />
		<strong>Text: </strong>
		<br />
		<textarea name="text" rows="8" cols="80">${page.text}</textarea>
		<br /><br />
		<input type="submit" value="Send">
	</form>
</td></tr></table>
<br />
<a href="/menu_trans">Return view translations</a>
