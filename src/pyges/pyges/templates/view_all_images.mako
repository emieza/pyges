<table>
	<tr>
		<td> TITLE </td>
		<td> ID </td>
		<td> IMAGE </td>
	</tr>
	% for image in pictures:
	<tr>
		<td>${image.title}</td>
		<td>${image.key().id()}</td>
		<td><img src="/view_picture/${image.key().id()}" /></td>
		
	</tr>
	% endfor

</table>