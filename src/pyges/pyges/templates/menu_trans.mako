<style type="text/css">
	#mt_tbl_table { border: 1px solid black; text-align:right; } /* table */
	.mt_tbl_row_0 { background-color: #fcf6cf; } /* title cell pair (td) */
	.mt_tbl_row_1 { background-color: #fdfcdc; } /* title cell add (td) */
	.mt_tbl_cel { padding: 10px; height: 110px; vertical-align: top; } /* each cell */
	.mt_tbl_sel { width: 130px; text-align: center; }
	.mt_tbl_hr_0 { color:#fdfcdc; background-color:#fdfcdc; height:1px; border:none; }
	.mt_tbl_hr_1 { color:#fcf6cf; background-color:#fcf6cf; height:1px; border:none; }
</style>
<script type="text/javascript">
	function select_option(sel){
		if (sel.options[sel.selectedIndex].value) {
			self.location = "/" + sel.name + "/" + sel.options[sel.selectedIndex].value;
		}
	}
</script>
<h1>Pyges: menu translations</h1>
<h3>description</h3>
<table id="mt_tbl_table" cellspacing="0px">
% for tbl in table:
	% if tbl['count']%2 == 0:
		<tr class="mt_tbl_row_0">
	% else:
		<tr class="mt_tbl_row_1">
	% endif
			<td class="mt_tbl_cel">
		% if tbl['id_en'] != "":
			${tbl['title_en']} (${langs['en']})
		% endif
		% if tbl['id_en'] != "" and tbl['id_es'] != "":
			% if tbl['count']%2 == 0:
				<hr class="mt_tbl_hr_0" />
			% else:
				<hr class="mt_tbl_hr_1" />
			% endif
		% endif
		% if tbl['id_es'] != "":
			${tbl['title_es']} (${langs['es']})
		% endif
		% if (tbl['id_en'] != "" and tbl['id_ca'] != "") or (tbl['id_es'] != "" and tbl['id_ca'] != ""):
			% if tbl['count']%2 == 0:
				<hr class="mt_tbl_hr_0" />
			% else:
				<hr class="mt_tbl_hr_1" />
			% endif
		% endif
		% if tbl['id_ca'] != "":
			${tbl['title_ca']} (${langs['ca']})
		% endif
		</td>
		<td class="mt_tbl_cel">
		% if tbl['id_en'] != "" or tbl['id_es'] != "" or tbl['id_ca'] != "":
			<select class="mt_tbl_sel" name="edit_trans" onchange="select_option(this)">
				<option value="" disabled="disabled" selected="selected">Edit</option>
			% if tbl['id_en'] != "":
				<option value="${tbl['id_en']}">${langs['en']}</option>
			% endif
			% if tbl['id_es'] != "":
				<option value="${tbl['id_es']}">${langs['es']}</option>
			% endif
			% if tbl['id_ca'] != "":
				<option value="${tbl['id_ca']}">${langs['ca']}</option>
			% endif
			</select>
		% else:
			&nbsp;
		% endif
		</td>
		<td class="mt_tbl_cel">
		% if tbl['id_en'] == "" or tbl['id_es'] == "" or tbl['id_ca'] == "":
			<select class="mt_tbl_sel" name="create_trans" onchange="select_option(this)">
				<option value="" disabled="disabled" selected="selected">Create</option>
			% if tbl['id_en'] == "":
				<option value="en/${tbl['idsec']}">${langs['en']}</option>
			% endif
			% if tbl['id_es'] == "":
				<option value="es/${tbl['idsec']}">${langs['es']}</option>
			% endif
			% if tbl['id_ca'] == "":
				<option value="ca/${tbl['idsec']}">${langs['ca']}</option>
			% endif
			</select>
		% else:
			&nbsp;
		% endif
		</td>
		<td class="mt_tbl_cel">
		% if tbl['id_en'] != "" or tbl['id_es'] != "" or tbl['id_ca'] != "":
			<select class="mt_tbl_sel" name="delete_trans" onchange="select_option(this)">
				<option value="" disabled="disabled" selected="selected">Delete</option>
			% if tbl['id_en'] != "":
				<option value="one/${tbl['id_en']}">${langs['en']}</option>
			% endif
			% if tbl['id_es'] != "":
				<option value="one/${tbl['id_es']}">${langs['es']}</option>
			% endif
			% if tbl['id_ca'] != "":
				<option value="one/${tbl['id_ca']}">${langs['ca']}</option>
			% endif
			% if (tbl['id_en'] != "" and  tbl['id_es'] != "") or (tbl['id_en'] != "" and  tbl['id_ca'] != "") or  (tbl['id_es'] != "" and  tbl['id_ca'] != ""):
			<option value="all/${tbl['idsec']}">All</option>
			% endif
			</select>
		% else:
			&nbsp;
		% endif
		</td>
	</tr>
% endfor
</table>
<br />
<a href="/">Return home</a>