<h1>Pyges: view translations</h1>

<table border="1" style="text-align:center;">
	<tr>
		<th>title</th>
		<th>english</th>
		<th>español</th>
		<th>català</th>
		<th>delete all</th>
	</tr>
	% for page in pages:
	<tr>
		<td rowspan="2">${page.title}</td>
		<td><a href="/create_trans/${page.key().id()}">yes</a></td>
		<td>no</td>
		<td>no</td>
		<td rowspan="2"><a href="/delete_trans/all/${page.key().id()}">delete</a></td>
	</tr>
	<tr>
		<td><a href="/delete_trans/one/${page.key().id()}">delete</a></td>
		<td><a href=""></a></td>
		<td><a href=""></a></td>
	</tr>
	% endfor
</table>


<ul>
    % for page in pages:
        <li><a href="/create_trans/${page.key().id()}">${page.title}</a> - ${langs[page.lang]}</li>
        % if page.jump:
        	<br />
        % endif
    % endfor
</ul>

<a href="/">Return home</a>.
