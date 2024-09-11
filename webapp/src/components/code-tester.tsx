'use client'

import { useState } from 'react'
import { Button } from "@/components/ui/button"
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from "@/components/ui/select"
import { Textarea } from "@/components/ui/textarea"
import { Input } from "@/components/ui/input"
import { Play, HelpCircle, X, Save, Send, LogOut } from "lucide-react"

export function CodeTester() {
  const [selectedLanguage, setSelectedLanguage] = useState('Spanish')

  return (
    <div className="flex flex-col h-screen bg-background text-foreground">
      <div className="flex flex-1 overflow-hidden">
        <div className="w-1/2 p-4 flex flex-col">
          <Textarea
            className="flex-1 bg-muted text-foreground placeholder-muted-foreground resize-none"
            placeholder="Put your code here..."
          />
        </div>
        <div className="w-1/2 p-4 flex">
          <div className="flex-1 flex flex-col">
            <div className="flex justify-between items-center mb-4">
              <h1 className="text-3xl font-bold">NoCodePython</h1>
            </div>
            <Textarea
              className="flex-1 bg-muted text-foreground mb-4 resize-none overflow-auto"
              readOnly
            />
            <div className="flex space-x-2">
              <Input className="flex-1 bg-muted text-foreground" />
              <Button variant="outline" size="icon">
                <Send className="h-4 w-4" />
              </Button>
            </div>
          </div>
          <div className="ml-4 flex flex-col space-y-2">
            <Button variant="outline" className="w-full">
              <Play className="h-4 w-4 mr-2" /> Run
            </Button>
            <Button variant="outline" className="w-full">
              <HelpCircle className="h-4 w-4 mr-2" /> Help
            </Button>
            <Button variant="outline" className="w-full">
              <X className="h-4 w-4 mr-2" /> Clear
            </Button>
            <Button variant="outline" className="w-full">
              <Save className="h-4 w-4 mr-2" /> Save
            </Button>
            <Select value={selectedLanguage} onValueChange={setSelectedLanguage}>
              <SelectTrigger className="w-full">
                <SelectValue placeholder="Select language" />
              </SelectTrigger>
              <SelectContent>
                <SelectItem value="Spanish">🇪🇸 Spanish</SelectItem>
                <SelectItem value="English">🇬🇧 English</SelectItem>
                <SelectItem value="French">🇫🇷 French</SelectItem>
              </SelectContent>
            </Select>
          </div>
        </div>
      </div>
      <div className="flex justify-between items-center p-4 bg-[#111111]">
        <span className="text-sm text-foreground">by MortalCoder</span>
      </div>
    </div>
  )
}
