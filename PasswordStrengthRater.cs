using System;

public class PasswordStrengthRater
{
    
    public static void Main(string[] args)
    {
        //strength rating will determine how good the password is
        int strengthRating = 0;
        int temp = 0;
        Console.WriteLine ("please enter the password you are concidering\n");
        //string to check
        string password = Console.ReadLine();
        Console.WriteLine("\n");
        string temppassword = password;
        temp = hasnums(temppassword);
        //adds strength based on number of numbers, up to three
        if (temp == 0)
        {
            Console.WriteLine("concider adding numbers\n");
        }
        else
        {
            strengthRating = strengthRating + temp;
        }
        
        //adds stregth based on length up to three
        if (password.Length > 20)
        {
            Console.WriteLine("Password Length is excelent!!\n");
            strengthRating = strengthRating + 3;
        }
        else if (password.Length > 10)
        {
            Console.WriteLine("Password Length is good!\n");
            strengthRating = strengthRating + 2;
        }
        else if (password.Length > 7)
        {
            Console.WriteLine("Password Length could be better!\n");
            strengthRating = strengthRating + 1;
        }
        else 
        {
            Console.WriteLine("Password is too short\n");
        }
        
        
        //adds two strength if contains a special char
        temp = hasspecials(temppassword);
        if (temp == 0)
        {
            Console.WriteLine("concider adding special chars\n");
        }
        else
        {
            strengthRating = strengthRating + 2;
        }
        
        
        //adds 2 strength if contains both upper and lower
        if (temppassword == temppassword.ToUpper() ||temppassword == temppassword.ToLower())
        {
            Console.WriteLine("use a mix of upper and lower case\n");
        }
        else
        {
            strengthRating = strengthRating + 2;
        }
        
        Console.WriteLine("the password you are rating: " + password + "\n");
        Console.WriteLine("your final rating was: " + strengthRating);
        if (strengthRating == 10)
            Console.WriteLine("Wow You achieved Maximum Strength");
        
        
    }
    static int hasnums(string temppassword)
    {
        int total = 0;
        foreach(var c in temppassword)
    {
        if (c is >= '0' and <= '9')
            total = total + 1;
    }
    
    if (total > 3)
        return 3;
    return total;
    }
    static int hasspecials(string temppassword)
    {
        foreach(var c in temppassword)
    {
        if (c is  '!' or  '@' or '#' or  '$' or  '%' or  '^' or  '&' or  '*' or  '(' or  ')')
            return 1;
    }
    return 0;
    }
}
