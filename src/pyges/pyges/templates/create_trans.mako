<h1>Pyges: create translate</h1>

<table>
	<tr>
		<td style="width:45%">
		    <h3>Language: ${langs[page.lang]}</h3>
		    <h2>Name: ${page.title}</h2>
		    <h2>Text:</h2>
		    <div>${page.text}</div>
		</td>
		<td style="width:10%"></td>
		<td style="width:45%">
		    <form method="post">
		        <input type="text" name="idsec" value="${page.idsec}" style="display:none;"/><br>
		        Language:<br>
		        <select name="lang">
		        % for l in langs:
		            <option value="${l}">${langs[l]}</option>
		        % endfor
		        </select>
		        <br>
		        Name:<br>
		        <input type="text" name="title" /><br>
		        Text:<br>
		        <textarea name="text" rows="8" cols="80"></textarea><br>
		        <input type="submit" value="Send">
		    </form>
		</td>
	</tr>
</table>
<br>
<a href="/">Return home</a>.
