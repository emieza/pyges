<style type="text/css">
	.ct_tbl_cel { border: 1px solid black; padding: 5px; width:50%;} /* each cell */
	.ct_tbl_div { width: 100%; height: 100%}
</style>
<script type="text/javascript">
	window.onload = first_sel;
	function first_sel(){
		value = document.getElementById("sel_lang").value;
		var ajax = new XMLHttpRequest();
		ajax.open("GET","../../view_trans/" + value + "/${idsec}",false);
		ajax.send();
		document.getElementById("view_trans").innerHTML = ajax.responseText;
	}
	function select_option(sel){
		var ajax = new XMLHttpRequest();
		ajax.open("GET","../../view_trans/" + sel.options[sel.selectedIndex].value + "/${idsec}",false);
		ajax.send();
		document.getElementById("view_trans").innerHTML = ajax.responseText;
	}
</script>
<h1>Pyges: create translation</h1>
<h3>description</h3>
<table>
	<tr>
		<td class="ct_tbl_cel">
			<br />
			<strong>Language: </strong>
			<select id="sel_lang" name="lang" onchange="select_option(this)">
			% for l in exl:
				<option value="${l}">${exl[l]}</option>
			% endfor
			</select>
			<br /><br />
			<div id="view_trans"></div>
			<br /><br />
		</td>
		<td class="ct_tbl_cel">
			% if len(exl) != 0:
				<form method="post">
					<input type="text" name="idsec" value="${idsec}" style="display:none;"/>
					<input type="text" name="lang" value="${ln}" style="display:none;" />
					<br />
					<strong>Language: </strong>
					${langs[ln]}
					<br /><br />
					<strong>Title: </strong>
					<input type="text" name="title" />
					<br /><br />
					<strong>Text: </strong>
					<br />
					<textarea name="text" rows="8" cols="80"></textarea>
					<br /><br />
					<input type="submit" value="Send">
				</form>
			% else:
				<div>All translations have been made</div>
			% endif
		</td>
	</tr>
</table>
<br />
<a href="/menu_trans">Return view translations</a>
