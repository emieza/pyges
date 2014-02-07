<style type="text/css">
	#vt_tbl_table { text-align:center; } /* table */
	#vt_tbl_table a { text-decoration: none; color: #000} /* table links */
	.vt_tbl_cel { border: 1px solid black; padding: 1px 5px; } /* each cell */
	.vt_tbl_head { background-color: #f1edc2; } /* table head */
	.vt_tbl_title_0 { background-color: #fdfcdc; } /* title cell pair (td) */
	.vt_tbl_title_1 { background-color: #fcf6cf; } /* title cell add (td) */
	.vt_tbl_edit { background-color: #eef3e2; } /* edit row (tr) */
	.vt_tbl_trans { background-color: #ecf1ef; } /* translatin row (tr) */
	.vt_tbl_del { background-color: #f6f0ed; } /* delete cel row (tr) */
</style>

<h1>Pyges: view translations</h1>
<h3>description</h3>
<table id="vt_tbl_table">
	% for tbl in table:
		% if tbl['count']%6 == 0:
			<tr class="vt_tbl_head">
				<th class="vt_tbl_cel" rowspan="2">Titles</th>
				<th class="vt_tbl_cel" colspan="3">Lenguages</th>
				<th class="vt_tbl_cel" rowspan="2">Page</th>
			</tr>
			<tr class="vt_tbl_head">
				<th class="vt_tbl_cel">${langs['en']}</th>
				<th class="vt_tbl_cel">${langs['es']}</th>
				<th class="vt_tbl_cel">${langs['ca']}</th>
			</tr>
		% endif
		<tr class="vt_tbl_edit">
		% if tbl['count']%2 == 0:
			<td class="vt_tbl_cel vt_tbl_title_0" rowspan="3">
		% else:
			<td class="vt_tbl_cel vt_tbl_title_1" rowspan="3">
		% endif
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
				<td class="vt_tbl_cel"><a href="/edit_trans/${tbl['id_en']}">edit</a></td>
			% else:
				<td class="vt_tbl_cel">&nbsp;</td>
			% endif
			% if tbl['id_es'] != "":
				<td class="vt_tbl_cel"><a href="/edit_trans/${tbl['id_es']}">edit</a></td>
			% else:
				<td class="vt_tbl_cel">&nbsp;</td>
			% endif
			% if tbl['id_ca'] != "":
				<td class="vt_tbl_cel"><a href="/edit_trans/${tbl['id_ca']}">edit</a></td>
			% else:
				<td class="vt_tbl_cel">&nbsp;</td>
			% endif
			<td class="vt_tbl_cel vt_tbl_del" rowspan="3"><a href="/delete_trans/all/${tbl['idsec']}">delete<br />all</a></td>
		</tr>
		<tr class="vt_tbl_trans">
			% if tbl['id_en'] != "":
				<td class="vt_tbl_cel"><a href="/create_trans/${tbl['id_en']}">create</a></td>
			% else:
				<td class="vt_tbl_cel">&nbsp;</td>
			% endif
			% if tbl['id_es'] != "":
				<td class="vt_tbl_cel"><a href="/create_trans/${tbl['id_es']}">create</a></td>
			% else:
				<td class="vt_tbl_cel">&nbsp;</td>
			% endif
			% if tbl['id_ca'] != "":
				<td class="vt_tbl_cel"><a href="/create_trans/${tbl['id_ca']}">create</a></td>
			% else:
				<td class="vt_tbl_cel">&nbsp;</td>
			% endif
		</tr>
		<tr class="vt_tbl_del">
			% if tbl['id_en'] != "":
				<td class="vt_tbl_cel"><a href="/delete_trans/one/${tbl['id_en']}">delete</a></td>
			% else:
				<td class="vt_tbl_cel">&nbsp;</td>
			% endif
			% if tbl['id_es'] != "":
				<td class="vt_tbl_cel"><a href="/delete_trans/one/${tbl['id_es']}">delete</a></td>
			% else:
				<td class="vt_tbl_cel">&nbsp;</td>
			% endif
			% if tbl['id_ca'] != "":
				<td class="vt_tbl_cel"><a href="/delete_trans/one/${tbl['id_ca']}">delete</a></td>
			% else:
				<td class="vt_tbl_cel">&nbsp;</td>
			% endif
		</tr>
	% endfor
</table>
<br />
<table id="vt_tbl_table">
	% for tbl in table:
		% if tbl['count']%6 == 0:
			<tr class="vt_tbl_head">
				<th class="vt_tbl_cel" rowspan="2">Titles</th>
				<th class="vt_tbl_cel" colspan="3">Lenguages</th>
				<th class="vt_tbl_cel" rowspan="2">Page</th>
			</tr>
			<tr class="vt_tbl_head">
				<th class="vt_tbl_cel">${langs['en']}</th>
				<th class="vt_tbl_cel">${langs['es']}</th>
				<th class="vt_tbl_cel">${langs['ca']}</th>
			</tr>
		% endif

	% endfor
</table>
<a href="/">Return home</a>
