<h1>Pyges: create translation</h1>
<h3>description</h3>
<table border="1">
	<tr>
		<td style="width:50%">
		    <div>Language: ${langs[page.lang]}</div>
		    <br />
		    <div>Name: ${page.title}</div>
		    <br />
		    <div>Text:</div>
		    <div>${page.text}</div>
		</td>
		<td style="width:50%">
			% if len(lop) != 0:
			    <form method="post">
			        <input type="text" name="idsec" value="${page.idsec}" style="display:none;"/><br>
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
