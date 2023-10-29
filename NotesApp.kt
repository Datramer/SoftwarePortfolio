import java.io.File
import java.io.FileWriter



class note(val filename: String?) {
    private var myfilename: String? = filename;

    fun printnote() {
        var myfileinfo: String? = File("C:\\Users\\josep\\IdeaProjects\\NOTEAPPTEST\\src\\main\\kotlin\\$myfilename.txt").readText(Charsets.UTF_8)
    println(myfileinfo)
    }
    fun savenote( texttosave: String?) {
        val myWriter = FileWriter("C:\\Users\\josep\\IdeaProjects\\NOTEAPPTEST\\src\\main\\kotlin\\$myfilename.txt")
        myWriter.write(texttosave.toString())
        myWriter.close()
    }
}

fun main(args: Array<String>) {
    println("enter your file name:")
    var mynewfilename= readLine()
    val note1 = note(mynewfilename)
    println("1- read\n2- write \n3- quit \n")
   var op : Int = 0
    while (op != 3){
    op= readLine()!!.toInt()
    when(op) {
        1 -> {
        note1.printnote()
        }

        2 -> {
            println("what would you like to write?:")
            val temp = readLine()
            note1.savenote(temp)

        }
    }
    }
    print ("thankyou for writing notes!")
    // Try adding program arguments via Run/Debug configuration.
    // Learn more about running applications: https://www.jetbrains.com/help/idea/running-applications.html.
    //println("Program arguments: ${args.joinToString()}")
}
