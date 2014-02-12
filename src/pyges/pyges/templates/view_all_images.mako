<!-- Table style -->

<style>
	td {
		width:100px;
		height:100px;
		border:1px solid black;
	}
	img {
		width:100%;
		height:100%;
	}
</style>

<!-- Generate table -->

<table>
	<tr>
		<th> TITLE </th>
		<th> ID </th>
		<th> IMAGE </th>
	</tr>
	% for image in pictures:
	<tr>
		<td>${image.title}</td>
		<td>${image.key().id()}</td>
		<td><img src="/view_picture/${image.key().id()}" /></td>
		
	</tr>
	% endfor

</table>