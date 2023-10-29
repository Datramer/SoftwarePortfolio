import java.io.File
import java.io.FileWriter


//notes class
class note(val filename: String?) {
    private var myfilename: String? = filename;
//used to printout the file
    fun printnote() {
        var myfileinfo: String? = File("C:\\Users\\josep\\IdeaProjects\\NOTEAPPTEST\\src\\main\\kotlin\\$myfilename.txt").readText(Charsets.UTF_8)
    println(myfileinfo)
    }
    //used to overwrite the file
    fun savenote( texttosave: String?) {
        val myWriter = FileWriter("C:\\Users\\josep\\IdeaProjects\\NOTEAPPTEST\\src\\main\\kotlin\\$myfilename.txt")
        myWriter.write(texttosave.toString())
        myWriter.close()
    }
}

fun main(args: Array<String>) {
    //enter the file name (no file type only name)
    println("enter your file name:")
    //accept input
    var mynewfilename= readLine()
    val note1 = note(mynewfilename)
    println("1- read\n2- write \n3- quit \n")
   var op : Int = 0
    //loop for continuing 
    while (op != 3){
    op= readLine()!!.toInt()
    when(op) {
        //if 1 show notes
        1 -> {
        note1.printnote()
        }
        //if 2 write over notes
        2 -> {
            println("what would you like to write?:")
            val temp = readLine()
            note1.savenote(temp)

        }
    }
    }
    //goodbye
    print ("thankyou for writing notes!")
}
