<style type="text/css">
	.ct_tbl_cel { border: 1px solid black; padding: 5px; width:50%;} /* each cell */
</style>

<h1>Pyges: create translation</h1>
<h3>description</h3>
<table>
	<tr>
		<td class="ct_tbl_cel">
			<strong>Language: </strong>${langs[page.lang]}
			<br />
			<strong>Title: </strong>${page.title}
			<br />
			<strong>Text: </strong>
			<div>${page.text}</div>
		</td>
		<td class="ct_tbl_cel">
			% if len(lop) != 0:
				<form method="post">
					<input type="text" name="idsec" value="${page.idsec}" style="display:none;"/>
					<br>
					Language: <select name="lang">
					% for l in lop:
						<option value="${l}">${lop[l]}</option>
					% endfor
					</select>
					<br><br>
					Title: <input type="text" name="title" />
					<br><br>
					Text: <br>
					<textarea name="text" rows="8" cols="80"></textarea>
					<br><br>
					<input type="submit" value="Send">
				</form>
			% else:
				<div>All translations have been made</div>
			% endif
		</td>
	</tr>
</table>
<br>
<a href="/view_trans">Return view translations</a>
