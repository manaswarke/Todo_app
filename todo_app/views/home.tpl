<html>
        <head>
                 <title>
                              Todo App by Kamal sir
                 </title>
                 <style>
                          * {
                                 font-size:30px;
                                 text-align:center;
                          }
                          body {
                                 background-color:azure;
                          }
                          textarea {
                                 resize:none;
                          }
                          table {
                                 margin:auto;
                                 width:60%
                          }
                 </style>
        </head>
        <body>            
                 <h1> Todo App</h1>
                 <form method = "POST">
                       <textarea
                              name = "task"
                              placeholder = "Enter Task details"
                              rows="3" 
                              cols="30"    
                              required
                       ></textarea>
                       <br/><br/>
                       <input type="submit"
                       />
                </form>

                       <table border="5">
                                <tr>
                                      <th> Task </th>
                                      <th> Delete </th>
                                </tr>
    
                       % for m in msg:
                             <tr>
                                      <td> {{ m[1] }} </td>
                                      <td> <a href="/delete/{{ m[0] }}">
                                         
                                         <button onclick="return confirm('r u sure???')"> Delete

</button></a></td>
                             </tr>
             % end
             </table>
        </body>
</html>
                     
 
                     
 
                           