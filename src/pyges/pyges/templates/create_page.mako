<h1>Pyges: create page</h1>

<form method="post">
	Language:
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