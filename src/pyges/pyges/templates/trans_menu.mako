<style type="text/css">
	#mt_tbl_table { border: 1px solid black; text-align:right; } /* table */
	.mt_tbl_row_0 { background-color: #eee; } /* title cell pair (td) */
	.mt_tbl_row_1 { background-color: #fff; } /* title cell add (td) */
	.mt_tbl_cel { padding: 10px; height: 110px; vertical-align: top; } /* each cell */
	.mt_tbl_sel { width: 130px; text-align: center; }
	.mt_tbl_hr_0 { color:#fff; background-color:#fff; height:1px; border:none; }
	.mt_tbl_hr_1 { color:#eee; background-color:#eee; height:1px; border:none; }
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
		% for lang in langs:
			% if tbl['title_' + lang] != "":
				${tbl['title_' + lang]} (${langs[lang]})
				% if tbl['last'] != lang:
					% if tbl['count']%2 == 0:
						<hr class="mt_tbl_hr_0"/>
					% else:
						<hr class="mt_tbl_hr_1"/>
					% endif
				% endif
			% endif
		% endfor
		</td>
		<td class="mt_tbl_cel">
			<select class="mt_tbl_sel" name="trans_edit" onchange="select_option(this)">
				<option value="" disabled="disabled" selected="selected">Edit</option>
			% for lang in langs:
				% if tbl['id_' + lang] != "":
					<option value="${tbl['id_' + lang]}">${langs[lang]}</option>
				% endif
			% endfor
			</select>
		</td>
		<td class="mt_tbl_cel">
		% if tbl['nlang'] < len(langs):
			<select class="mt_tbl_sel" name="trans_create" onchange="select_option(this)">
				<option value="" disabled="disabled" selected="selected">Create</option>
			% for lang in langs:
				% if tbl['id_' + lang] == "":
					<option value="${lang}/${tbl['idsec']}">${langs[lang]}</option>
				% endif
			% endfor
			</select>
		% else:
			&nbsp;
		% endif
		</td>
		<td class="mt_tbl_cel">
			<select class="mt_tbl_sel" name="trans_delete" onchange="select_option(this)">
				<option value="" disabled="disabled" selected="selected">Delete</option>
			% for lang in langs:
				% if tbl['id_' + lang] != "":
					<option value="one/${tbl['id_' + lang]}">${langs[lang]}</option>
				% endif
			% endfor
			% if tbl['nlang'] > 1:
			<option value="all/${tbl['idsec']}">All</option>
			% endif
			</select>
		</td>
	</tr>
% endfor
</table>
<br />
<a href="/">Return home</a>