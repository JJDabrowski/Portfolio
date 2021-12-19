//
//  DLController.swift
//  Lotto2
//
//  Created by Swantewit on 18/09/2021.
//

import UIKit

class DLController: UIViewController {

    override func viewDidLoad() {
        super.viewDidLoad()

        // Do any additional setup after loading the view.
        
    }
    
    @IBOutlet weak var fResult:UILabel!
    
    //A function to randomize the X numbers from Y set
    
    func iterateNremove() -> (Set<Int>, Set<Int>){
        var nums = Set<Int>(1...49)
        var reslts = Set<Int>()
        for _ in 1...6{
            let randNum = nums.randomElement()!
            reslts.insert(randNum)
            nums.remove(randNum)
        }
    return (nums, reslts)
    }


    @IBAction func randomize(_ sender: Any) {
        
        //call the randomizing function and the first Set from its results
        let go = iterateNremove()
        let res = go.1
        
        //change set to String without square brackets
        let strng = res.map(String.init).joined(separator: ", ")
        
        fResult.text = strng
        
    }
    
    
    @IBAction func switchViews(_ sender: UIButton){
    }
    
    @IBAction func wroc(_ sender: Any) {
    }
    /*
    // MARK: - Navigation

    // In a storyboard-based application, you will often want to do a little preparation before navigation
    override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
        // Get the new view controller using segue.destination.
        // Pass the selected object to the new view controller.
    }
    */

}
