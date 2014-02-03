<h1>Pyges: create translation</h1>

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
		    <form method="post">
		        <input type="text" name="idsec" value="${page.idsec}" style="display:none;"/><br>
		        Language: <select name="lang">
		        % for l in langs:
		            <option value="${l}">${langs[l]}</option>
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
		</td>
	</tr>
</table>
<br>
<a href="/">Return home</a>.
