<h1>Pyges: create translate</h1>


<table>
<tr>
<td>
    <form method="post">
	  id: <span> id de la pàgina </span>
	  
	  <br/>
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
</td>

<td>
      <form method="post">
	      
	      
	      id: <span> id de la pàgina </span>
	      
	      <br/>
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
</td>
</tr>
</table>
