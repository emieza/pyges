<form action="updatecss" method="post">
<select name="skinselect">
	% for skin in listskins:
		<option value="${skin.id}">${skin.nom}</option>
	% endfor
	<input type="submit" value="Editar la skin"/>
</select>
</form>
<a href="/">Tornar enrere</a>

