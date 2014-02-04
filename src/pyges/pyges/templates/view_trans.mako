<h1>Pyges: view translations</h1>
<h3>description</h3>
<table border="1" style="text-align:center;">
	<tr>
		<th>Titles</th>
		<th colspan="3">Languages</th>
		<th>Page</th>
	</tr>
	% for tbl in table:
		<tr>
			<td rowspan="2">
			% if tbl['id_en'] != "":
				${tbl['title_en']}
			% endif
			% if tbl['id_en'] != "" and tbl['id_es'] != "":
				<br />
			% endif
			% if tbl['id_es'] != "":
				${tbl['title_es']}
			% endif
			% if (tbl['id_en'] != "" and tbl['id_ca'] != "") or (tbl['id_es'] != "" and tbl['id_ca'] != ""):
				<br />
			% endif
			% if tbl['id_ca'] != "":
				${tbl['title_ca']}
			% endif
			</td>
			% if tbl['id_en'] != "":
				<td><a href="/create_trans/${tbl['id_en']}">${langs['en']}</a></td>
			% else:
				<td>&nbsp;</td>
			% endif
			% if tbl['id_es'] != "":
				<td><a href="/create_trans/${tbl['id_es']}">${langs['es']}</a></td>
			% else:
				<td>&nbsp;</td>
			% endif
			% if tbl['id_ca'] != "":
				<td><a href="/create_trans/${tbl['id_ca']}">${langs['ca']}</a></td>
			% else:
				<td>&nbsp;</td>
			% endif
			<td rowspan="2"><a href="/delete_trans/all/${tbl['idsec']}">delete<br />all</a></td>
		</tr>
		<tr>
			% if tbl['id_en'] != "":
				<td><a href="/delete_trans/one/${tbl['id_en']}">delete</a></td>
			% else:
				<td>&nbsp;</td>
			% endif
			% if tbl['id_es'] != "":
				<td><a href="/delete_trans/one/${tbl['id_es']}">delete</a></td>
			% else:
				<td>&nbsp;</td>
			% endif
			% if tbl['id_ca'] != "":
				<td><a href="/delete_trans/one/${tbl['id_ca']}">delete</a></td>
			% else:
				<td>&nbsp;</td>
			% endif
		</tr>
	% endfor
</table>
<br />
<a href="/">Return home</a>
